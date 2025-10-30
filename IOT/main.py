import uuid
import os
import logging
import random
import time

from dotenv import load_dotenv
from core.infrastructure.message.kafka_message_publisher import KafkaMessagePublisher
from core.domain.message.message import Message
from core.domain.metric.metric import Metric

from core.domain.common.value_objects.temperature import Temperature , TEMP_UNIT_CEL
from core.domain.common.value_objects.humidity import Humidity
from core.domain.common.value_objects.device import Device
from core.domain.common.value_objects.timestamp import TimeStamp

##Load env
load_dotenv('.env')
KAFKA_HOST=os.getenv('KAFKA_HOST')
KAFKA_USER=os.getenv('KAFKA_USER')
KAFKA_PASSWD=os.getenv('KAFKA_PASSWD')
KAFKA_TOPIC=os.getenv('KAFKA_TOPIC')
KAFKA_CLIENT_ID=os.getenv('KAFKA_CLIENT_ID')
SENSOR_TIME_SYNC=os.getenv('SENSOR_TIME_SYNC')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

#simluate sensors
sensors = [
    Device(no=str(uuid.uuid4()),name="north-sensor"),
    Device(no=str(uuid.uuid4()),name="south-sensor"),
    Device(no=str(uuid.uuid4()),name="chamber-a-sensor"),
    Device(no=str(uuid.uuid4()),name="chamber-b-sensor"),
]

##prepare publisher
publisher = KafkaMessagePublisher(
    bootstrap_servers=[KAFKA_HOST],
    username=KAFKA_USER,
    password=KAFKA_PASSWD,
    client_id=KAFKA_CLIENT_ID
)

try:

    while(True):
        for sensor in sensors:
            #Generate random metric
            temp = Temperature(value=random.randrange(15,75),unit=TEMP_UNIT_CEL)
            humidity = Humidity(value=random.randrange(10,60))
            metric = Metric(datetime=TimeStamp.now(),temp=temp,humidity=humidity,device=sensor)    
            
            #prepare metric
            msg = Message( datetime=TimeStamp.now(),  context="test", metric=metric)
            publisher.publish(topic=KAFKA_TOPIC,message=msg)
        time.sleep(int(SENSOR_TIME_SYNC))
except KeyboardInterrupt:
    logging.info("🛑 Simulación detenida por el usuario.")
finally:
    publisher.close()
    logging.info("✅ Publisher cerrado correctamente.")
