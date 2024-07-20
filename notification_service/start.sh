#!/bin/sh

# Start the Django development server in the background
python manage.py runserver 0.0.0.0:8000 &

# Wait for the Django server to be ready
./wait-for-it.sh localhost 8000 --timeout=30

# Start the Kafka consumer in the foreground
python manage.py consume_events
