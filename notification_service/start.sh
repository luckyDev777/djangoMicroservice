#!/bin/sh

# Start the Django development server
python manage.py runserver 0.0.0.0:8000 &

# Start the Kafka consumer
python manage.py consume_events
