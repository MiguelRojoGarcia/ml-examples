from dataclasses import dataclass

@dataclass(frozen=True)
class Humidity:
    value:float
    def __str__(self) -> str:
        return f"{self.value}"