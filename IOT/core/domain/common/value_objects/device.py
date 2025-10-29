from dataclasses import dataclass
from typing import Optional
from enum import Enum
from datetime import datetime


class DeviceType(str, Enum):
    SENSOR = "sensor"
    ACTUATOR = "actuator"
    GATEWAY = "gateway"

@dataclass(frozen=True)
class Device:
    no:str
    name:str
    type: DeviceType = DeviceType.SENSOR
    model: Optional[str] = None
    registered_at: Optional[datetime] = None

    def __str__(self) -> str:
        return f"{self.name} ({self.no}) - {self.type}"
    
    def __eq__(self, other):
        return self.no == other
    
    def __hash__(self):
        return self.no