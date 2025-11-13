import logging
from core.domain.metric.metric import Metric
from core.domain.message.message import Message
from core.domain.common.value_objects.timestamp import TimeStamp
from core.domain.metric.i_metric_repository import IMetricRepository

logger = logging.getLogger(__name__)

class RunTrainer:

    _metricRepository:IMetricRepository

    def __init__(self,metricRepository: IMetricRepository):       
        self._metricRepository = metricRepository       
        
    def handle(self, batchSize:int = 100) -> None:       
        try:
            pass
        
        except Exception as e:
            logger.exception(f"❌ Error guardando métrica en MongoDB: {e}")
            raise