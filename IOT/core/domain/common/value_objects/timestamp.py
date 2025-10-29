from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class TimeStamp:
    value:datetime
       
    @classmethod
    def now(cls):
        return cls(datetime.now(timezone.utc))
    
    def __str__(self) -> str:
        return self.to_iso()