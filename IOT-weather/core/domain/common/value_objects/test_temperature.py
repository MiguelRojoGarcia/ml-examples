import pytest

from core.domain.common.value_objects.temperature import Temperature
from core.domain.common.value_objects.temperature import TEMP_UNIT_CEL

def test_instance_temperature():    
    temp = Temperature(value=12,unit=TEMP_UNIT_CEL)
    assert isinstance(temp, Temperature)
