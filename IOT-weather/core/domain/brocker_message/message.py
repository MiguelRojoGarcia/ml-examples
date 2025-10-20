from dataclasses import dataclass
from core.domain.common.value_objects.timestamp import TimeStamp

@dataclass(frozen=True)
class Message:
    _datetime: TimeStamp
    _context: str
    _metadata: dict
    _message:dict
    
    def __str__(self) -> str:
        return print(f"[{self.datetime}][{self._context}]{self.message} ( {self._message} )")