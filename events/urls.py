from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('dashboard/', views.home, name='dashboard'),
    path("add_event/", views.add_event, name="add_event"),
    path("delete-event/<int:id>", views.delete_event, name="delete_event"),
    path("update-event/<int:id>", views.update_event, name="update_event"),
    path("do-update-event/<int:id>", views.do_update_event, name="do_update_event"),
]