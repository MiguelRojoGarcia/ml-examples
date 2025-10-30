import logging
from pymongo import MongoClient
from core.domain.metric.metric import Metric
from core.domain.metric.i_metric_repository import IMetricRepository
logger = logging.getLogger(__name__)


class MongoMetricRepository(IMetricRepository):

    def __init__(
        self,
        uri: str,
        database: str,
        collection: str,
    ):
       
        self._client = MongoClient(uri)
        self._db = self._client[database]
        self._collection = self._db[collection]

        logger.info(
            f"MongoMetricRepository conectado a {uri}, base de datos '{database}', colección '{collection}'."
        )

    def save(self, metric: Metric) -> None:
       
        try:
            self._collection.insert_one(metric.to_dict())
            logger.debug(f"✅ Métrica guardada")
        except Exception as e:
            logger.exception(f"❌ Error guardando métrica en MongoDB: {e}")
            raise
  
    def close(self):
        self._client.close()
