from core.domain.message.message import Message
from core.domain.metric.metric import Metric
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.common.value_objects.temperature import Temperature
from core.domain.common.value_objects.device import Device
from core.domain.common.value_objects.humidity import Humidity

def test_instance_message():    
    temp = Temperature(value=12)
    humidity = Humidity(value=74)
    metric = Metric(datetime=TimeStamp.now(),temp=temp,humidity=humidity,device="test-device")
    message = Message(
        datetime=TimeStamp.now(),
        context="unit-test",
        metadata={},
        metric=metric
    )
    assert isinstance(message, Message)
    print(f"dict: {message.to_dict()}")



