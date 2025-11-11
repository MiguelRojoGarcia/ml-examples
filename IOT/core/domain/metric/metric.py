from dataclasses import dataclass , asdict
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.common.value_objects.temperature import Temperature
from core.domain.common.value_objects.humidity import Humidity
from core.domain.device.device import Device
from core.domain.common.value_objects.milk_litters import MilkLitters

@dataclass(frozen=True)
class Metric:
    cow_id: str
    device_id: str
    milk_litters: MilkLitters
    datetime: TimeStamp
    temp: Temperature
    humidity: Humidity
    
    def __str__(self) -> str:
        return print(f"[{self.datetime.value}][{self.device_id}]{self.milk_litters.value}")    
    
    def to_dict(self):
        d = asdict(self)
        d["datetime"] = self.datetime.value.isoformat()
        return d
    
    @staticmethod
    def from_dict(data: dict) -> "Metric":
        return Metric(
            cow_id=data["cow_id"],
            device_id=data["device_id"],
            milk_litters=MilkLitters(**data["milk_litters"]),
            datetime=TimeStamp.from_dict(data["datetime"]),
            temp=Temperature(**data["temp"]),
            humidity=Humidity(**data["humidity"]),
        )