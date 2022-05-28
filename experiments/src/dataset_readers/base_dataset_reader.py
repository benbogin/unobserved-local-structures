import json
import logging
from random import Random
from typing import Dict, Optional, Iterable

from allennlp.data.dataset_readers.dataset_reader import DatasetReader
from allennlp.data.fields import TextField, MetadataField
from allennlp.data.instance import Instance
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer
from allennlp.data.tokenizers import Tokenizer, WhitespaceTokenizer
from overrides import overrides

logger = logging.getLogger(__name__)


@DatasetReader.register("base_dataset_reader")
class BaseDatasetReader(DatasetReader):
    def __init__(
        self,
        split_path: str = None,
        source_tokenizer: Tokenizer = None,
        target_tokenizer: Tokenizer = None,
        source_token_indexers: Dict[str, TokenIndexer] = None,
        target_token_indexers: Dict[str, TokenIndexer] = None,
        source_max_tokens: Optional[int] = None,
        target_max_tokens: Optional[int] = None,
        skip_source_too_long: bool = False,
        skip_target_too_long: bool = False,
        truncate_source_too_long: bool = False,
        read_loops: int = 1,
        n_train_sample: int = None,
        n_test_sample: int = None,
        sample_random_seed: int = 0,
        instance_source: str = "source",
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self._split_path = split_path
        self._source_tokenizer = source_tokenizer or WhitespaceTokenizer()
        self._target_tokenizer = target_tokenizer or self._source_tokenizer
        self._source_token_indexers = source_token_indexers or {
            "tokens": SingleIdTokenIndexer()
        }
        self._target_token_indexers = (
            target_token_indexers or self._source_token_indexers
        )

        self._source_max_tokens = source_max_tokens
        self._target_max_tokens = target_max_tokens
        self._skip_source_too_long = skip_source_too_long
        self._skip_target_too_long = skip_target_too_long
        self._truncate_source_too_long = truncate_source_too_long

        self._read_loops = read_loops

        self._n_train_sample = n_train_sample
        self._n_test_sample = n_test_sample

        self._random = Random(sample_random_seed)

        self._instance_source = instance_source

    def get_examples(self, file_path, is_train: bool):
        all_examples = [json.loads(s) for s in open(file_path, "rt")]

        if self._split_path:
            split_info = json.load(open(self._split_path, "rt"))
            train_ids = set(split_info.get("train") or split_info.get("train_examples"))
            test_ids = set(split_info.get("test") or split_info.get("test_examples"))

            if is_train:
                all_examples = [ex for ex in all_examples if ex["qid"] in train_ids]
            else:
                all_examples = [ex for ex in all_examples if ex["qid"] in test_ids]

        assert len(all_examples) > 0
        return all_examples

    @overrides
    def _read(self, file_path: str) -> Iterable[Instance]:
        is_test = file_path.startswith("@")
        if is_test:
            file_path = file_path[1:]
        is_train = not is_test

        all_examples = self.get_examples(file_path, is_train)
        original_size = len(all_examples)

        if (
            self._n_train_sample
            and is_train
            and len(all_examples) > self._n_train_sample
        ):
            all_examples = self._random.sample(all_examples, self._n_train_sample)
        elif (
            self._n_test_sample
            and not is_train
            and len(all_examples) > self._n_test_sample
        ):
            # we want test sampling to be the same no matter the training seed - so we use a separate random object
            sampling_random = Random(0)
            all_examples = sampling_random.sample(all_examples, self._n_test_sample)

        print(
            f"\nTrying to load {len(all_examples)} {'train' if is_train else 'test'} examples "
            f"(original size was {original_size})"
        )

        # read the training data multiple times - this is optional, and just to save on evaluation time
        read_loops = self._read_loops if not is_test else 1
        for _ in range(read_loops):
            for line in all_examples:
                instance = self.text_to_instance(line)
                if instance:
                    yield instance

    def get_schema_string(self, ex) -> str:
        return ""

    @overrides
    def text_to_instance(self, ex) -> Optional[Instance]:
        source = ex[self._instance_source].lower() + " "
        tokenized_source = self._source_tokenizer.tokenize(source)

        if self._source_max_tokens and len(tokenized_source) > self._source_max_tokens:
            if self._skip_source_too_long:
                return None
            if self._truncate_source_too_long:
                # truncate tokens up to maximum size(include start/end of sentence tokens)
                tokenized_source = (
                    [tokenized_source[0]]
                    + tokenized_source[1 : self._source_max_tokens - 1]
                    + [tokenized_source[-1]]
                )
            else:
                raise Exception(
                    f"Source is of length {len(tokenized_source)}, which is longer than source_max_tokens"
                    f" of {self._source_max_tokens}"
                )
        source_field = TextField(tokenized_source, self._source_token_indexers)

        metadata = {"ex_qid": ex["qid"], "source": source}

        fields = {
            "source_tokens": source_field,
        }

        if ex.get("target"):
            target = metadata["target"] = ex.get("target")
            metadata["anonymized_target"] = ex.get("anonymized")

            tokenized_target = self._target_tokenizer.tokenize(target)

            # if self._target_max_tokens and len(tokenized_target) > self._target_max_tokens:
            #     if self._skip_target_too_long:
            #         return None
            #     else:
            #         raise Exception(f"Target is of length {len(tokenized_target)}, which is longer than target_max_tokens"
            #                         f" of {self._target_max_tokens}")

            target_field = TextField(tokenized_target, self._target_token_indexers)

            fields["target_tokens"] = target_field

        fields["metadata"] = MetadataField(metadata)

        return Instance(fields)
