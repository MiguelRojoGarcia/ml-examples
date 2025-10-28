import pytest

from core.domain.common.value_objects.temperature import Temperature
from core.domain.common.value_objects.temperature import TEMP_UNIT_CEL

def test_instance_temperature():    
    temp = Temperature(value=12,unit=TEMP_UNIT_CEL)
    assert isinstance(temp, Temperature)

def test_compare_temperature():    
    temp_a = Temperature(value=25,unit=TEMP_UNIT_CEL)
    temp_b = Temperature(value=35,unit=TEMP_UNIT_CEL)
   
    assert temp_a < temp_b
    assert temp_b > temp_a
    assert temp_b == temp_b
    assert temp_b >= temp_b
    assert temp_b <= temp_b

def test_below_zero():    
    below_zero_temp = Temperature(value=-15,unit=TEMP_UNIT_CEL)
    assert below_zero_temp.is_below_zero
    
    
