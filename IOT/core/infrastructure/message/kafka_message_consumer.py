import json
import logging
from confluent_kafka import Consumer, KafkaError, KafkaException
from core.domain.message.message import Message

logger = logging.getLogger(__name__)


class KafkaMetricConsumer:

    def __init__(
        self,
        bootstrap_servers: list[str],
        group_id: str,
        topic: str,
        auto_offset_reset: str = "earliest",
    ):
      
        conf = {
            "bootstrap.servers": ",".join(bootstrap_servers),
            "group.id": group_id,
            "auto.offset.reset": auto_offset_reset,
            "enable.auto.commit": True,
        }

        self._consumer = Consumer(conf)
        self._topic = topic

        logger.info(f"✅ KafkaMetricConsumer inicializado (topic={topic}, group={group_id})")

    def consume(self, timeout: float = 1.0) -> Message | None:
     
        msg = self._consumer.poll(timeout)
        if msg is None:
            return None

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                return None
            raise KafkaException(msg.error())

        try:
            payload = json.loads(msg.value().decode("utf-8"))

            message = (
                Message.from_dict(payload)
                if hasattr(Message, "from_dict")
                else Message(**payload)
            )

            logger.debug(f"✅ Métrica recibida: {message}")
            return message

        except Exception as e:
            logger.exception(f"❌ Error deserializando mensaje: {e}")
            return None

    def consume_forever(self, callback):
       
        try:
            self._consumer.subscribe([self._topic])
            logger.info(f"📡 Suscrito al topic '{self._topic}'")

            while True:
                metric = self.consume()
                if metric:
                    callback(metric)

        except KeyboardInterrupt:
            logger.info("🛑 Consumidor interrumpido por el usuario.")
        finally:
            self.close()

    def close(self):
        """Cierra la conexión del consumidor."""
        logger.info("Cerrando consumidor Kafka...")
        self._consumer.close()
        logger.info("✅ Consumidor cerrado correctamente.")
