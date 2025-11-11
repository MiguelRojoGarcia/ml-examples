import pytest
import uuid
from core.domain.device.device import Device , DeviceType

def test_instance():    
    no = str(uuid.uuid4())
    device_sensor = Device(no=no,name="test-sensor-001")
    assert isinstance(device_sensor, Device)
    assert device_sensor.type == DeviceType.ELECTRIC
    assert device_sensor.no == no

def test_device_comparsion():    
    device_a = Device(no=str(uuid.uuid4()),name="device-a-001")
    device_b = Device(no=str(uuid.uuid4()),name="device-b-001")
    assert device_a == device_a
    assert device_a != device_b
    