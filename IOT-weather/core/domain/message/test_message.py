from core.domain.message.message import Message
from core.domain.common.value_objects.timestamp import TimeStamp

def test_instance_message():    
    message = Message(
        datetime=TimeStamp.now(),
        context="unit-test",
        metadata={},
        message={"test":"A","date":TimeStamp.now()}
    )
    assert isinstance(message, Message)

