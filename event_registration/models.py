from django.db import models

# Create your models here.

class RegisteredEvent(models.Model):

    event_id = models.IntegerField()
    event_title = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)