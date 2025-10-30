import os
import logging
from dotenv import load_dotenv
from core.infrastructure.message.kafka_message_consumer import KafkaMetricConsumer
from core.domain.message.message import Message
from core.domain.metric.metric import Metric


##Load env
load_dotenv('.env')

#common variables
KAFKA_HOST=os.getenv('KAFKA_HOST')
KAFKA_TOPIC=os.getenv('KAFKA_TOPIC')
KAFKA_GROUP_ID=os.getenv('KAFKA_GROUP_ID')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

##prepare consumer
consumer = KafkaMetricConsumer(
    bootstrap_servers=[KAFKA_HOST],
    group_id=KAFKA_GROUP_ID,
    topic=KAFKA_TOPIC
)

def process_metric(message:Message) :
    print(f"📥 Recibido {message.metric}")

try:

    consumer.consume_forever(callback=process_metric)
   
except KeyboardInterrupt:
    logging.info("🛑 Simulación detenida por el usuario.")
finally:
    consumer.close()
    logging.info("✅ Publisher cerrado correctamente.")
