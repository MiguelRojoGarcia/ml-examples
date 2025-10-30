import uuid
from core.domain.metric.metric import Metric
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.common.value_objects.temperature import Temperature , TEMP_UNIT_CEL
from core.domain.common.value_objects.humidity import Humidity
from core.domain.common.value_objects.device import Device

def test_instance_metric():    
    temp = Temperature(value=12,unit=TEMP_UNIT_CEL)
    humidity = Humidity(value=74)
    device_sensor = Device(no=str(uuid.uuid4()),name="test-sensor-001")
    metric = Metric(datetime=TimeStamp.now(),temp=temp,humidity=humidity,device=device_sensor)    
   
    assert isinstance(metric, Metric)

def test_negative_metric():    
    temp = Temperature(value=-12,unit=TEMP_UNIT_CEL)
    humidity = Humidity(value=74)
    device_sensor = Device(no=str(uuid.uuid4()),name="test-sensor-001")
    metric = Metric(datetime=TimeStamp.now(),temp=temp,humidity=humidity,device=device_sensor)    
    assert isinstance(metric, Metric)
    assert metric.temp.value < 0 

def test_to_dict():    
    temp = Temperature(value=-12,unit=TEMP_UNIT_CEL)
    humidity = Humidity(value=74)
    metric = Metric(datetime=TimeStamp.now(),temp=temp,humidity=humidity,device="test-device")    
    print(f"dict: {metric.to_dict()}")
    