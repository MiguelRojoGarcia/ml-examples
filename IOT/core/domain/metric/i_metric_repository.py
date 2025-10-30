from abc import abstractmethod
from typing import Protocol
from core.domain.metric.metric import Metric

class IMetricRepository(Protocol):
    @abstractmethod
    def save(self, metric: Metric) -> None:
        pass