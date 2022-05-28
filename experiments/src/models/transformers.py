from typing import Optional, Dict, Any

from allennlp.modules.transformer.util import IntT
from allennlp.training.metrics.average import Average
from overrides import overrides
import torch

from allennlp.data import TextFieldTensors, Vocabulary
from allennlp.data.tokenizers import PretrainedTransformerTokenizer
from allennlp.models.model import Model

from .bart_wrapper import Bart
from .t5_wrapper import T5Wrapper


@Model.register("cfg_transformers")
class Transformers(Model):
    def __init__(
        self,
        vocab: Vocabulary,
        model_name: str,
        beam_size: int = 3,
        max_decoding_steps=100,
        **kwargs
    ) -> None:
        super().__init__(vocab, **kwargs)
        self._model_name = model_name
        # We only instantiate this when we need it.
        self._tokenizer: Optional[PretrainedTransformerTokenizer] = None

        if "t5" in model_name:
            self.model = T5Wrapper(
                vocab,
                model_name,
                max_decoding_steps=max_decoding_steps,
                beam_size=beam_size,
            )
        elif "bart" in model_name:
            self.model = Bart(
                model_name,
                vocab,
                max_decoding_steps=max_decoding_steps,
                beam_size=beam_size,
            )
        else:
            raise ValueError()

        self._metrics_accuracy = Average()

    @property
    def tokenizer(self) -> PretrainedTransformerTokenizer:
        if self._tokenizer is None:
            self._tokenizer = PretrainedTransformerTokenizer(self._model_name)
        return self._tokenizer

    def forward(  # type: ignore
        self,
        source_tokens: TextFieldTensors,
        target_tokens: Optional[TextFieldTensors] = None,
        metadata: Dict = None,
    ) -> Dict[str, torch.Tensor]:
        """
        Performs the forward step of T5.

        # Parameters

        source_tokens : `TextFieldTensors`, required
            The source tokens for the encoder. We assume they are stored under the `tokens` key/namespace.

        target_tokens : `TextFieldTensors`, optional (default = `None`)
            The target tokens for the decoder. We assume they are also stored under the `tokens` key/namespace.
            If no target tokens are given during training / validation, the source tokens are shifted
            to the right by 1.

        # Returns

        `Dict[str, torch.Tensor]`
            Contains the `loss` when `target_tokens` is provided.
            And during prediction, includes `predictions` and `predicted_log_probs` from beam search.

        """
        input_ids, attention_mask = (
            source_tokens["tokens"]["token_ids"],
            source_tokens["tokens"]["mask"],
        )
        labels: Optional[IntT] = None

        if target_tokens is not None:
            labels, decoder_attention_mask = (
                target_tokens["tokens"]["token_ids"],
                target_tokens["tokens"]["mask"],
            )
        elif self.training:
            raise ValueError("'target_tokens' required during training")

        output_dict = self.model(source_tokens, target_tokens)

        if not self.training:
            if labels is not None:
                output_dict["source_text"] = self.make_output_human_readable(input_ids)
                output_dict["predicted_text"] = self.make_output_human_readable(
                    output_dict["predictions"]
                )
                output_dict["correct"] = []
                output_dict["qid"] = [md["ex_qid"] for md in metadata]
                output_dict["source_text"] = [md["source"] for md in metadata]
                output_dict["gold_text"] = [md["target"] for md in metadata]

                gold_tokenized_text = self.make_output_human_readable(labels)

                for p, l in zip(output_dict["predicted_text"], gold_tokenized_text):
                    correct = p == l
                    self._metrics_accuracy(correct)
                    output_dict["correct"].append(correct)

        return output_dict

    @overrides
    def make_output_human_readable(self, sequence) -> Dict[str, Any]:
        decoded_batch = self.tokenizer.tokenizer.batch_decode(
            sequence, skip_special_tokens=True
        )
        for i, output in enumerate(decoded_batch):
            # just a small hack to fix tokenizer issue with exclamation marks that appear as first chars in words
            decoded_batch[i] = output.replace("string!", "string !")
        return decoded_batch

    @overrides
    def get_metrics(self, reset: bool = False) -> Dict[str, float]:
        return {"accuracy": self._metrics_accuracy.get_metric(reset=reset)}
