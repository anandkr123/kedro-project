import logging
import time
from typing import Any

from kedro.framework.hooks import hook_impl
from kedro.pipeline.node import Node


class LoggingHook:
    """A hook that logs how many time it takes to load each dataset."""

    def __init__(self):
        self._timers = {}

    @property
    def _logger(self):
        return logging.getLogger(__name__)

    @hook_impl
    def before_dataset_loaded(self, dataset_name: str, node: Node) -> None:
        start = time.time()
        self._timers[dataset_name] = start

    @hook_impl
    def after_dataset_loaded(self, dataset_name: str, data: Any, node: Node) -> None:
        start = self._timers[dataset_name]
        end = time.time()
        self._logger.info(
            "Loading dataset %s before node '%s' takes %0.2f seconds",
            dataset_name,
            node.name,
            end - start,
        )

