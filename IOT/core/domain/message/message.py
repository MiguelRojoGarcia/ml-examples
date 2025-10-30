from dataclasses import dataclass , asdict
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.common.value_objects.temperature import Temperature
from core.domain.common.value_objects.humidity import Humidity
from core.domain.common.value_objects.device import Device
from core.domain.metric.metric import Metric
from typing import Optional

@dataclass(frozen=True)
class Message:
    datetime: TimeStamp
    context: str
    metric: Metric
    metadata: Optional[dict] = None

    def to_dict(self):
        d = asdict(self)
        d["datetime"] = self.datetime.value.isoformat()
        d["metric"] = self.metric.to_dict()
        return d