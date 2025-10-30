import logging
from pymongo import MongoClient
from core.domain.metric.metric import Metric
from core.domain.metric.i_metric_repository import IMetricRepository
logger = logging.getLogger(__name__)


class MongoMetricRepository(IMetricRepository):

    def __init__(
        self,
        uri: str = "mongodb://mongodb:27017",
        database: str = "iot",
        collection: str = "metrics",
    ):
       
        self._client = MongoClient(uri)
        self._db = self._client[database]
        self._collection = self._db[collection]

        logger.info(
            f"MongoMetricRepository conectado a {uri}, base de datos '{database}', colección '{collection}'."
        )

    def save(self, metric: Metric) -> None:
       
        try:
            document = (
                metric.to_dict()
                if hasattr(metric, "to_dict")
                else metric.__dict__
            )

            self._collection.insert_one(document)
            logger.debug(f"✅ Métrica guardada: {document}")
        except Exception as e:
            logger.exception(f"❌ Error guardando métrica en MongoDB: {e}")
            raise
  
    def close(self):
        self._client.close()
