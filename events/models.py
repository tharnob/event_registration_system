from django.db import models

# Create your models here.
class Event(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField(max_length=150)
    location_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)


