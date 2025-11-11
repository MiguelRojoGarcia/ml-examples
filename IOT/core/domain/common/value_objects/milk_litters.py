from dataclasses import dataclass

@dataclass(frozen=True)
class MilkLitters:
    value:float
    def __str__(self) -> str:
        return f"{self.value}"