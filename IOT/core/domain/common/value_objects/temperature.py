from dataclasses import dataclass
from typing import Optional

TEMP_UNIT_CEL   = "C"
TEMP_UNIT_FA    = "F"

@dataclass(frozen=True)
class Temperature:
    value:float
    unit: Optional[str] =  TEMP_UNIT_CEL   
    
    def __str__(self) -> str:
        return f"{self.value} {self.unit}"
      
    def __eq__(self, other):
        return self.value == other
    
    #>
    def __gt__(self, other):
        return self.value > other    
    def __lt__(self, other):
        return self.value < other
    
    # >=
    def __ge__(self, other):
        return self.value >= other    
    def __le__(self, other):
        return self.value <= other
    
    @property
    def is_below_zero(self):
        return  self.value < 0


