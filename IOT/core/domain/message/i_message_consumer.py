from abc import ABC, abstractmethod
from typing import Protocol

class IMessageConsumer(Protocol):
    @abstractmethod
    def consume(self, topic: str) -> None:
        """Consume topic."""
        pass