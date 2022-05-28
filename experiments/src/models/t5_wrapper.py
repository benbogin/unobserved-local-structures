from typing import Optional, Dict

import torch
from allennlp.data import Vocabulary, TextFieldTensors
from allennlp.models import Model
from allennlp.modules.transformer.util import IntT, BoolT

from .t5_module import T5 as T5Module, T5Output


class T5Wrapper(Model):
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
        self.model = T5Module.from_pretrained_module(
            model_name, beam_size=beam_size, max_decoding_steps=max_decoding_steps
        )

    def forward(  # type: ignore
        self,
        source_tokens: TextFieldTensors,
        target_tokens: Optional[TextFieldTensors] = None,
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
        decoder_attention_mask: Optional[BoolT] = None
        if target_tokens is not None:
            labels, decoder_attention_mask = (
                target_tokens["tokens"]["token_ids"],
                target_tokens["tokens"]["mask"],
            )
        elif self.training:
            raise ValueError("'target_tokens' required during training")

        output: T5Output = self.model(
            input_ids,
            attention_mask=attention_mask,
            labels=labels,
            decoder_attention_mask=decoder_attention_mask,
        )
        output_dict: Dict[str, torch.Tensor] = {}

        if self.training:
            assert output.loss is not None
            output_dict["loss"] = output.loss
        else:
            # Shape: (batch_size, beam_size, num_tokens)
            assert output.predictions is not None
            # Shape: (batch_size, beam_size)
            assert output.predicted_log_probs is not None
            # Shape: (batch_size, num_tokens)
            output_dict["predictions"] = output.predictions[:, 0, :]
            # Shape: (batch_size, )
            output_dict["predicted_log_probs"] = output.predicted_log_probs[:, 0]

            if labels is not None:
                assert output.loss is not None
                output_dict["loss"] = output.loss

        return output_dict
