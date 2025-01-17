from django.db import models

class Notification(models.Model):
    recipient_id = models.IntegerField() 
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for User {self.recipient_id}'
