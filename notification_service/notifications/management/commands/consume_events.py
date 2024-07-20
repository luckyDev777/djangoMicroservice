from django.core.management.base import BaseCommand
import logging
from kafka import KafkaConsumer
from notifications.models import Notification
import json


logger = logging.getLogger(__name__)


def consume_events():
    try:
        consumer = KafkaConsumer(
            "post.created",
            bootstrap_servers="kafka:9092",
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="notification_group",
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        )
        logger.info(
            "Kafka consumer initialized and subscribed to 'post.created' topic."
        )

        for message in consumer:
            try:
                event_data = message.value
                recipient_id = event_data["author_id"]
                message_text = f"New post created with title {event_data['title']}"

                Notification.objects.create(
                    recipient_id=recipient_id, message=message_text
                )
                logger.info(
                    f"Notification created for recipient_id={recipient_id}: {message_text}"
                )
            except Exception as e:
                logger.error(
                    f"Error processing message: {message.value}. Error: {str(e)}"
                )
    except Exception as e:
        logger.error(f"Failed to initialize Kafka consumer. Error: {str(e)}")


class Command(BaseCommand):
    help = "Consume Kafka events"

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        logger.info("Starting Kafka consumer...")
        consume_events()
        logger.info("Kafka consumer stopped.")
