from dataclasses import dataclass
from core.domain.common.value_objects.timestamp import TimeStamp

TEMP_UNIT_CEL   = "C"
TEMP_UNIT_FA    = "F"


@dataclass(frozen=True)
class Metric:
    datetime: TimeStamp
    temp: float
    temp_unit: str
    humidity: float
    device_no: str
    
    def __str__(self) -> str:
        return print(f"[{self.datetime}][{self.device_no}]{self.temp}/{self.humidity}")