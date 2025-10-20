import pytest
from core.domain.metric.metric import Metric, TEMP_UNIT_CEL
from core.domain.common.value_objects.timestamp import TimeStamp


def test_instance_metric():    
    metric = Metric(datetime=TimeStamp.now(),temp=12,humidity=74,device_no="test-device",temp_unit=TEMP_UNIT_CEL)    
    assert isinstance(metric, Metric)

def test_negative_metric():    
    metric = Metric(datetime=TimeStamp.now(),temp=-12,humidity=74,device_no="test-device",temp_unit=TEMP_UNIT_CEL)    
    assert isinstance(metric, Metric)
    assert metric.temp < 0 