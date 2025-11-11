from dataclasses import dataclass
from core.domain.common.value_objects.timestamp import TimeStamp

@dataclass(frozen=True)
class TimeRange:
    from_date:TimeStamp
    to_date:TimeStamp
       
    def __str__(self) -> str:
        return print(f"{self.from_date.to_iso()} - {self.to_date.to_iso()}")

    def to_dict(self) -> dict:
        return {"from_date": self.from_date.to_iso(),"to_date":self.to_date.to_iso}
    