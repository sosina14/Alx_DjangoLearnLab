from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        notifications = request.user.notifications.all().order_by('-timestamp')
        data = [
            {
                "id": notifications.id,
                "actor": notifications.actor.username,
                "verb": notifications.verb,
                "target": str(notifications.target),
                "timestamp": notifications.timestamp,
                "read": notifications.read,
            }
            for notification in notifications
        ]
        return Response(data)
    def post(self, request):  # Mark all notifications as read
        request.user.notifications.update(read=True)
        return Response({'message': "All notifications marked as read"})
