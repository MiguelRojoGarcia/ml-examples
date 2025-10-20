from abc import ABC, abstractmethod
from typing import Protocol
from core.domain.message.message import Message

class IMessagePublisher(Protocol):
    @abstractmethod
    def publish(self, topic: str, message: Message) -> None:
        """Publish message in the provided topic."""
        pass