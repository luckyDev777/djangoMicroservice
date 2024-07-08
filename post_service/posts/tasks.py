import requests
from celery import shared_task

@shared_task
def send_notification(recipiend_id, message):
    notification_service_url = f'http://notification-service:8000/notification/'
    payload = {"recipient_id": recipiend_id, "message": message}
    response = requests.post(notification_service_url, data=payload)
    if response.status_code != 204:
        return "Something went wrong!"
    return "Successfully created!"