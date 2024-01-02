from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('dashboard/<int:id>', views.event_registration_page, name='user_dashboard'),
    path("add_registration/", views.event_registration, name="add_registration"),
    path("registered_event/", views.registered_event, name="registered_event"),
    path("delete-registration/<int:id>", views.delete_registration, name="delete_registration"),



    path('api/', views.api_root),
    path('api/registered_events/', views.RegEvents.as_view(), name='registered-events'),
    path('api/reg_detail/<int:pk>/', views.RegDetail.as_view(), name="registeredevent-detail"),
])