from dataclasses import dataclass , asdict
from core.domain.common.value_objects.timestamp import TimeStamp

@dataclass(frozen=True)
class Cow:
    cow_id: str
    name: str
    cow_birth_date: TimeStamp
    last_birth_date: TimeStamp

    def __str__(self) -> str:
        return print(f"[{self.cow_id}]{self.name}")    
    
    def to_dict(self):
        d = asdict(self)
        d["cow_birth_date"] = self.cow_birth_date.value.isoformat()
        d["last_birth_date"] = self.last_birth_date.value.isoformat()
        return d
    
    @staticmethod
    def from_dict(data: dict) -> "Cow":
        return Cow(
            cow_id=data["cow_id"],
            name=data["name"],
            cow_birth_date=TimeStamp.from_dict(data["cow_birth_date"]),
            last_birth_date=TimeStamp.from_dict(data["last_birth_date"]),
        )