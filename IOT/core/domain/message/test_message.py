from core.domain.message.message import Message
from core.domain.metric.metric import Metric
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.common.value_objects.temperature import Temperature , TEMP_UNIT_CEL
from core.domain.common.value_objects.humidity import Humidity
from core.domain.common.value_objects.milk_litters import MilkLitters
import uuid

def test_instance_message():    
    temp = Temperature(value=12,unit=TEMP_UNIT_CEL)
    humidity = Humidity(value=74)
    sensor_id = uuid.uuid4().hex
    cow_id = uuid.uuid4().hex
    metric = Metric(
        cow_id=cow_id,
        device_id=sensor_id,
        milk_litters=MilkLitters(value=15.5),
        datetime=TimeStamp.now(),
        temp=temp,
        humidity=humidity)   
  
    message = Message(
        datetime=TimeStamp.now(),
        context="unit-test",
        metadata={},
        metric=metric
    )

    assert isinstance(message, Message)

def test_to_dict():    
    temp = Temperature(value=12,unit=TEMP_UNIT_CEL)
    humidity = Humidity(value=74)
    sensor_id = uuid.uuid4().hex
    cow_id = uuid.uuid4().hex
    milk_litters=MilkLitters(value=15.5)
    metric = Metric(
        cow_id=cow_id,
        device_id=sensor_id,
        milk_litters=MilkLitters(value=15.5),
        datetime=TimeStamp.now(),
        temp=temp,
        humidity=humidity)   
   
    message = Message(
        datetime=TimeStamp.now(),
        context="unit-test",
        metadata={},
        metric=metric
    )
    message_dict = message.to_dict()
    assert isinstance(message_dict, dict)
    assert message_dict["context"] == "unit-test"
    assert message_dict["metric"]["cow_id"] == cow_id
    assert message_dict["metric"]["device_id"] == sensor_id
    assert message_dict["metric"]["milk_litters"]["value"] == milk_litters.value
    assert message_dict["metric"]["temp"]["value"] == temp.value
    assert message_dict["metric"]["temp"]["unit"] == TEMP_UNIT_CEL
    assert message_dict["metric"]["humidity"]["value"] == humidity.value