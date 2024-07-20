import json
from kafka import KafkaProducer

def publish_event(event_name, event_data):
    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(event_name, event_data)
    producer.flush()
    producer.close()
    return "Event published!"
