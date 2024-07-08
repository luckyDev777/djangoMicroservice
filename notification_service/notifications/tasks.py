from celery import shared_task
from .models import Notification

@shared_task
def create_notification(recipient_id, message):
    Notification.objects.create(recipient_id=recipient_id, message=message)
