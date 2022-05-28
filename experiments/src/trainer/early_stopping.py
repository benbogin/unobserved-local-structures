import json
from typing import Dict, Any, List, Optional

import os

import numpy
import torch
from allennlp.common.util import sanitize

from allennlp.training.callbacks.callback import TrainerCallback
from allennlp.data import TensorDict


@TrainerCallback.register("early_stopping")
class EarlyStoppingCallback(TrainerCallback):
    def __init__(self, serialization_dir: str, stop_at_accuracy=0.99):
        super().__init__(serialization_dir)
        self._stop_at_accuracy = stop_at_accuracy
        self._should_stop = False

    def on_epoch(
        self,
        trainer: "GradientDescentTrainer",
        metrics: Dict[str, Any],
        epoch: int,
        is_primary: bool = True,
        **kwargs,
    ) -> None:
        if metrics["validation_accuracy"] > self._stop_at_accuracy:
            # we don't want to raise an exception here since then the trainer won't get to save this checkpoint
            self._should_stop = True

    def on_batch(
        self,
        trainer: "GradientDescentTrainer",
        batch_inputs: List[TensorDict],
        batch_outputs: List[Dict[str, Any]],
        batch_metrics: Dict[str, Any],
        epoch: int,
        batch_number: int,
        is_training: bool,
        is_primary: bool = True,
        batch_grad_norm: Optional[float] = None,
        **kwargs,
    ) -> None:
        if self._should_stop:
            raise Exception("Reached stopping accuracy")
