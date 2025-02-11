from django.conf import settings
from django.db import models
from django.utils.timezone import now

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Correct reference
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # This should be fine as long as you provide a default for old rows

    def __str__(self):
        return self.title
