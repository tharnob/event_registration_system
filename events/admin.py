from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "event_date", "event_time", "location_name", "slot", "created_at",)

admin.site.register(Event, EventAdmin)
