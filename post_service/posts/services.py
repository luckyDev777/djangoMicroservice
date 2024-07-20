import json
import time
import logging
from kafka import KafkaProducer, KafkaConsumer, TopicPartition, OffsetAndMetadata

logger = logging.getLogger(__name__)


class KafkaService:
    def __init__(self, bootstrap_servers="kafka:9092"):
        self.bootstrap_servers = bootstrap_servers

    def produce_message(self, topic, message):
        producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        producer.send(topic, message)
        producer.flush()
        producer.close()

    def consume_message(self, topic, user_id, timeout=10):
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset="earliest",
            enable_auto_commit=False,
            group_id="post_service_group",
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        )

        start_time = time.time()
        for message in consumer:
            response_message = message.value
            if response_message.get("user_id") == user_id:
                tp = TopicPartition(message.topic, message.partition)
                consumer.commit({tp: OffsetAndMetadata(message.offset + 1, None)})
                logger.info(f"Acknowledged message for user_id={user_id}")
                consumer.close()
                return response_message
            if time.time() - start_time > timeout:
                break
        consumer.close()
        return None
