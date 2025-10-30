from dataclasses import dataclass , asdict
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.metric.metric import Metric
from typing import Optional

@dataclass(frozen=True)
class Message:
    datetime: TimeStamp
    context: str
    metric: Metric
    metadata: Optional[dict] = None

    def __str__(self) -> str:
        return print(f"[{self.datetime}][{self._context}]{self.message} ( {self._message} )")

    def to_dict(self):
        d = asdict(self)
        d["datetime"] = self.datetime.value.isoformat()
        d["metric"] = self.metric.to_dict()
        return d