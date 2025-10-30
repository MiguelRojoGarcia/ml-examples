import logging
import json
from typing import Optional
from confluent_kafka import Producer
from core.domain.message.message import Message
from core.domain.message.i_message_publisher import IMessagePublisher

logger = logging.getLogger(__name__)

class KafkaMessagePublisher(IMessagePublisher):
    def __init__(
        self,
        bootstrap_servers: list[str],
        username: Optional[str] = "",
        password: Optional[str] = "",
    ):
        
        config = {
            "bootstrap.servers": ",".join(bootstrap_servers),
            "client.id": "iot-producer",
            'security.protocol': 'PLAINTEXT',
            'acks':'all'
        }

        if username != "":
            config["security.protocol"] = "SASL_SSL"
            config["sasl.mechanisms"] = "PLAIN"
            config["sasl.username"] = username
            config["sasl.password"] = password
        
        self._producer = Producer(config)

        logger.info(f"✅ Conexión establecida a servidor '{bootstrap_servers}'")


    def publish(self, topic: str, message: Message) -> None:

        try:
           
            payload = message.to_dict() if hasattr(message, "to_dict") else vars(message)
           
            key = None

            if hasattr(message, "metric") and hasattr(message.metric, "device"):
                key = message.metric.device.no

            self._producer.produce(
                topic=topic,
                key=key,
                value=json.dumps(payload).encode("utf-8"),
                callback=self._delivery_callback,
            )

            self._producer.poll(0)

            logger.info(f"✅ Mensaje publicado correctamente en topic '{topic}'")
        except BufferError:
            logger.warning("⚠️  Buffer lleno, esperando a que se vacíe...")
            self._producer.poll(1)
        except Exception as e:
            logger.exception(f"❌ Error publicando mensaje en Kafka: {e}")
            raise
    
    def _delivery_callback(self,err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

    def close(self):
        logger.info("Cerrando productor Kafka (flushing pending messages)...")
        self._producer.flush(timeout=10)
