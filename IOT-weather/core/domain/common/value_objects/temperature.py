from dataclasses import dataclass

TEMP_UNIT_CEL   = "C"
TEMP_UNIT_FA    = "F"

@dataclass(frozen=True)
class Temperature:
    value:float
    unit: str
    
    def __str__(self) -> str:
        return f"{self.value} {self.unit}"