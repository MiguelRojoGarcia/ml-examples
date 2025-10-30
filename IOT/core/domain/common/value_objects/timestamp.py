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

    def to_iso(self) -> str:
        return self.value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")

    def to_dict(self) -> dict:
        return {"value": self.to_iso()}

    @staticmethod
    def from_dict(data: dict) -> "TimeStamp":
        if isinstance(data, datetime):
            return TimeStamp(data)

        value = data.get("value") if isinstance(data, dict) else data

        if isinstance(value, str):
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        elif isinstance(value, datetime):
            parsed = value
        else:
            raise TypeError(f"Valor inválido para TimeStamp: {value}")

        return TimeStamp(parsed)