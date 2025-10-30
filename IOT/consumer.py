import os
import logging
from dotenv import load_dotenv
from core.infrastructure.message.kafka_message_consumer import KafkaMetricConsumer
from core.infrastructure.message.kafka_message_publisher import KafkaMessagePublisher

from core.domain.message.message import Message
from core.application.metric.save_metric import SaveMetric
from core.infrastructure.metric.mongo_metric_repository import MongoMetricRepository

##Load env
load_dotenv('.env')

#common variables
KAFKA_HOST=os.getenv('KAFKA_HOST')
KAFKA_TOPIC=os.getenv('KAFKA_TOPIC')
KAFKA_GROUP_ID=os.getenv('KAFKA_GROUP_ID')
KAFKA_USER=os.getenv('KAFKA_USER')
KAFKA_PASSWD=os.getenv('KAFKA_PASSWD')
KAFKA_CLIENT_ID=os.getenv('KAFKA_CLIENT_ID')

MONGO_URI=os.getenv('MONGO_URI')
MONGO_DATABASE=os.getenv('MONGO_DATABASE')
MONGO_COLLECTION=os.getenv('MONGO_COLLECTION')

logging.basicConfig(level=logging.INFO,format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

client = MongoMetricRepository(uri=MONGO_URI,database=MONGO_DATABASE,collection=MONGO_COLLECTION)
consumer = KafkaMetricConsumer(bootstrap_servers=[KAFKA_HOST],group_id=KAFKA_GROUP_ID,topic=KAFKA_TOPIC)

save_metric_publisher = KafkaMessagePublisher(bootstrap_servers=[KAFKA_HOST],username=KAFKA_USER,password=KAFKA_PASSWD,client_id=KAFKA_CLIENT_ID)
save_metric_handler = SaveMetric(messagePublisher=save_metric_publisher,metricRepository=client)

def process_metric(message:Message) :
    print(f"📥 Recibido {message.metric}")
    save_metric_handler.handle(metric=message.metric)

try:

    consumer.consume_forever(callback=process_metric)
   
except KeyboardInterrupt:
    logging.info("🛑 Simulación detenida por el usuario.")
finally:
    consumer.close()
    logging.info("✅ Publisher cerrado correctamente.")
