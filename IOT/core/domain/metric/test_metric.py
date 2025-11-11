import uuid
from core.domain.metric.metric import Metric
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.common.value_objects.temperature import Temperature , TEMP_UNIT_CEL
from core.domain.common.value_objects.humidity import Humidity
from core.domain.common.value_objects.milk_litters import MilkLitters

def test_instance_metric():    
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
   
    assert isinstance(metric, Metric)

def test_to_dict():    
    temp = Temperature(value=12,unit=TEMP_UNIT_CEL)
    humidity = Humidity(value=74)
    sensor_id = uuid.uuid4().hex
    cow_id = uuid.uuid4().hex
    milk_litters=MilkLitters(value=15.5)
    metric = Metric(
        cow_id=cow_id,
        device_id=sensor_id,
        milk_litters=milk_litters,
        datetime=TimeStamp.now(),
        temp=temp,
        humidity=humidity)   

    metric_dict = metric.to_dict()
    assert isinstance(metric_dict, dict)
    assert metric_dict["cow_id"] == cow_id
    assert metric_dict["device_id"] == sensor_id
    assert metric_dict["milk_litters"]["value"] == milk_litters.value
    assert metric_dict["temp"]["value"] == temp.value
    assert metric_dict["temp"]["unit"] == TEMP_UNIT_CEL
    assert metric_dict["humidity"]["value"] == humidity.value
    