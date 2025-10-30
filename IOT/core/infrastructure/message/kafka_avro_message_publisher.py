import logging
import json
from kafka import KafkaProducer
from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from core.domain.message.message import Message
from core.domain.message.i_message_publisher import IMessagePublisher

logger = logging.getLogger(__name__)

class KafkaAvroMessagePublisher(IMessagePublisher):
   
        def __init__(
            self,
            bootstrap_servers: list[str],
            schema_registry_url: str,
            username: str,
            password: str,
        ):
            self._schema_registry_client = SchemaRegistryClient({"url": schema_registry_url})

            with open("core/infrastructure/message/avro/metric.avsc") as f:
                schema_str = f.read()

            self._avro_serializer = AvroSerializer(
                schema_registry_client=self._schema_registry_client,
                schema_str=schema_str,
            )

            self._producer = SerializingProducer(
                {
                    "bootstrap.servers": ",".join(bootstrap_servers),
                    "sasl.username": username,
                    "sasl.password": password,
                    
                    "security.protocol": "SASL_SSL",
                    "sasl.mechanisms": "PLAIN",
                    "acks": "all",
                    
                    "value.serializer": self._avro_serializer,
                    "key.serializer": str.encode,
                }
        )
            logger.info(f"KafkaMessagePublisher initialized for servers: {bootstrap_servers}")


        def publish(self, topic: str, message: Message) -> None:
            
            try:
            
                self._producer.produce(topic=topic, key=message.device.no, value=message.to_dict())
            
                self._producer.flush()
            
                logger.info(f"✅ Métrica publicada correctamente en topic '{topic}'")

            except Exception as e:
                logger.exception(f"❌ Error publicando métrica en Kafka: {e}")
                raise

        def close(self):
            logger.info("Cerrando productor Kafka...")
            self._producer.flush()