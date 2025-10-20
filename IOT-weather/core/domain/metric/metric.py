from dataclasses import dataclass
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.common.value_objects.temperature import Temperature
from core.domain.common.value_objects.humidity import Humidity

@dataclass(frozen=True)
class Metric:
    datetime: TimeStamp
    temp: Temperature
    humidity: Humidity
    device: str
    
    def __str__(self) -> str:
        return print(f"[{self.datetime}][{self.device}]{self.temp}")