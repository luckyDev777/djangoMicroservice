from kafka import KafkaConsumer
from .models import Notification
import json

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
