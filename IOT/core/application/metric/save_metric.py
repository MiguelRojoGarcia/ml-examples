import logging
from core.domain.metric.metric import Metric
from core.domain.message.message import Message
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.metric.i_metric_repository import IMetricRepository
from core.domain.message.i_message_publisher import IMessagePublisher

logger = logging.getLogger(__name__)

class SaveMetric:

    _metricRepository:IMetricRepository

    _messagePublisher:IMessagePublisher

    def __init__(self,metricRepository: IMetricRepository,messagePublisher:IMessagePublisher):       
        self._metricRepository = metricRepository       
        self._messagePublisher = messagePublisher       
        
    def handle(self, metric: Metric) -> None:       
        try:
            self._metricRepository.save(metric=metric)            
            domain_event = Message(datetime=TimeStamp.now(),context="domain-metric",metric=metric)
            self._messagePublisher.publish(topic="new-metric-stored",message=domain_event)            
        except Exception as e:
            logger.exception(f"❌ Error guardando métrica en MongoDB: {e}")
            raise