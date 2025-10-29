import pytest
import uuid
from core.domain.common.value_objects.device import Device , DeviceType

def test_instance_sensor():    
    no = str(uuid.uuid4())
    device_sensor = Device(no=no,name="test-sensor-001")
    assert isinstance(device_sensor, Device)
    assert device_sensor.type == DeviceType.SENSOR
    assert device_sensor.no == no

def test_instance_actuator():    
    no = str(uuid.uuid4())
    device_sensor = Device(no=no,name="test-actuator-001",type=DeviceType.ACTUATOR)
    assert isinstance(device_sensor, Device)
    assert device_sensor.type == DeviceType.ACTUATOR
    assert device_sensor.no == no

def test_instance_gateway():    
    no = str(uuid.uuid4())
    device_sensor = Device(no=no,name="test-gateway-001",type=DeviceType.GATEWAY)
    assert isinstance(device_sensor, Device)
    assert device_sensor.type == DeviceType.GATEWAY
    assert device_sensor.no == no

def test_device_comparsion():    
    device_a = Device(no=str(uuid.uuid4()),name="device-a-001")
    device_b = Device(no=str(uuid.uuid4()),name="device-b-001")
    assert device_a == device_a
    assert device_a != device_b
    