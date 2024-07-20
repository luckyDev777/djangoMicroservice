from django.core.management.base import BaseCommand
from notifications.tasks import consume_events
import logging

from kafka import KafkaConsumer
from notifications.models import Notification
import json
import logging

def consume_events():
    consumer = KafkaConsumer(
        'post.created',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='notification_group',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )
    for message in consumer:
        event_data = message.value
        recipient_id = event_data['author_id']
        message = f"New post created with title {event_data['title']}"
        Notification.objects.create(recipient_id=recipient_id, message=message)

class Command(BaseCommand):
    help = 'Consume Kafka events'

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info("Starting Kafka consumer...")
        consume_events()
        logger.info("Kafka consumer stopped.")
