from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.viewsets import ModelViewSet


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer