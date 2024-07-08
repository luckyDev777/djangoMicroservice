import requests
from celery import shared_task

@shared_task
def send_notification(recipient_id, message):
    notification_service_url = f'http://notification-service:8000/notifications/'
    payload = {"recipient_id": recipient_id, "message": message}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(notification_service_url, json=payload, headers=headers)
    if response.status_code != 201:
        return f"Something went wrong! Status code: {response.status_code}, Response: {response.text}"
    return "Successfully created!"
