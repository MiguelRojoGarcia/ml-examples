from abc import ABC, abstractmethod
from typing import Protocol
from core.domain.message.message import Message

class IMessageConsumer(Protocol):
    @abstractmethod
    def consume(self, topic: str) -> None:
        """Consume topic."""
        pass