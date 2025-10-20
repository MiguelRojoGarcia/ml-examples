from dataclasses import dataclass
from core.domain.common.value_objects.timestamp import TimeStamp

@dataclass(frozen=True)
class Message:
    datetime: TimeStamp
    context: str
    metadata: dict
    message:dict
    
    def __str__(self) -> str:
        return print(f"[{self.datetime}][{self._context}]{self.message} ( {self._message} )")