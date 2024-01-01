from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/<int:id>', views.event_registration_page, name='user_dashboard'),
    path("add_registration/", views.event_registration, name="add_registration"),
    path("registered_event/", views.registered_event, name="registered_event"),
    path("delete-registration/<int:id>", views.delete_registration, name="delete_registration"),
]