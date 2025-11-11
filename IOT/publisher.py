import os
import logging
import uuid
import time
import random
from dotenv import load_dotenv
from core.infrastructure.message.kafka_message_publisher import KafkaMessagePublisher
from core.domain.message.message import Message
from core.domain.metric.metric import Metric

from core.domain.common.value_objects.temperature import Temperature , TEMP_UNIT_CEL
from core.domain.common.value_objects.humidity import Humidity
from core.domain.device.device import Device
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.common.value_objects.milk_litters import MilkLitters

##Load env
load_dotenv('.env')

#common variables
KAFKA_HOST=os.getenv('KAFKA_HOST')
KAFKA_USER=os.getenv('KAFKA_USER')
KAFKA_PASSWD=os.getenv('KAFKA_PASSWD')
KAFKA_TOPIC=os.getenv('KAFKA_TOPIC')
KAFKA_CLIENT_ID=os.getenv('KAFKA_CLIENT_ID')

SENSOR_TIME_SYNC=os.getenv('SENSOR_TIME_SYNC')
SENSOR_NO=os.getenv('SENSOR_NO')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

##prepare publisher
publisher = KafkaMessagePublisher(bootstrap_servers=[KAFKA_HOST],username=KAFKA_USER,password=KAFKA_PASSWD,client_id=KAFKA_CLIENT_ID)

logging.info(f"Sensor {SENSOR_NO} activado")

cows = {
    "cow-001":"sensor-001",
    "cow-002":"sensor-002",
    "cow-003":"sensor-003",
    "cow-004":"sensor-004",
    "cow-005":"sensor-005"
}

milk_cycles = {cow: 0 for cow in cows}

try:
    
    while(True):

        for cow_id, sensor_id in cows.items():
            
            milk_cycles[cow_id] += 1

            #Generate random metric
            temp = Temperature(value=round(random.uniform(37.5, 39.2), 2), unit=TEMP_UNIT_CEL)
            humidity = Humidity(value=random.randint(55, 85))

            milk = None
            if milk_cycles[cow_id] % 3 == 0:
                milk = MilkLitters(value=round(random.uniform(6, 14), 2))

            metric = Metric(
                cow_id=cow_id,
                device_id=sensor_id,
                datetime=TimeStamp.now(),
                temp=temp,
                humidity=humidity,
                milk_litters=milk
            ) 
            
            #publish message
            msg = Message( datetime=TimeStamp.now(),  context="test", metric=metric)
            publisher.publish(topic=KAFKA_TOPIC,message=msg)       
                
            time.sleep(int(SENSOR_TIME_SYNC))
except KeyboardInterrupt:
    logging.info("🛑 Simulación detenida por el usuario.")
finally:
    publisher.close()
    logging.info("✅ Publisher cerrado correctamente.")
