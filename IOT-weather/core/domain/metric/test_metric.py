import pytest
from core.domain.metric.metric import Metric, TEMP_UNIT_CEL
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.common.value_objects.temperature import Temperature , TEMP_UNIT_CEL
from core.domain.common.value_objects.humidity import Humidity

def test_instance_metric():    
    temp = Temperature(value=12,unit=TEMP_UNIT_CEL)
    humidity = Humidity(value=74)
    metric = Metric(datetime=TimeStamp.now(),temp=temp,humidity=humidity,device_no="test-device")    
   
    assert isinstance(metric, Metric)

def test_negative_metric():    
    temp = Temperature(value=-12,unit=TEMP_UNIT_CEL)
    humidity = Humidity(value=74)
    metric = Metric(datetime=TimeStamp.now(),temp=temp,humidity=humidity,device_no="test-device")    
    assert isinstance(metric, Metric)
    assert metric.temp < 0 