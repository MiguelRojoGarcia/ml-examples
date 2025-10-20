from dataclasses import dataclass
from core.domain.metric.metric import Metric

@dataclass(frozen=True)
class AddNewMetric:    
    def Add(metrict: Metric) -> None:
        pass

