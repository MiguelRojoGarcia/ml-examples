from dataclasses import dataclass , asdict
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.common.value_objects.temperature import Temperature
from core.domain.common.value_objects.humidity import Humidity
from core.domain.common.value_objects.device import Device

@dataclass(frozen=True)
class Metric:
    datetime: TimeStamp
    temp: Temperature
    humidity: Humidity
    device: Device
    
    def __str__(self) -> str:
        return print(f"[{self.datetime.value}][{self.device.no}]{self.temp.value}")    
    
    def to_dict(self):
        d = asdict(self)
        d["datetime"] = self.datetime.value.isoformat()
        return d
    
    @staticmethod
    def from_dict(data: dict) -> "Metric":
        return Metric(
            datetime=TimeStamp.from_dict(data["datetime"])
            if hasattr(TimeStamp, "from_dict")
            else TimeStamp(**data["datetime"]),
            temp=Temperature(**data["temp"]),
            humidity=Humidity(**data["humidity"]),
            device=Device(**data["device"]),
        )