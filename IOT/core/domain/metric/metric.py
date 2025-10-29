from dataclasses import dataclass
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
        