from django.db import models
from users.models import CustomUser

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages', default=1)
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages', default=1)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # Fixed the indentation here
    archived = models.BooleanField(default=False)  # Fixed the indentation here

    def __str__(self):
        return f'{self.subject} - {self.sender} to {self.recipient}'
