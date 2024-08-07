from django.urls import path

from . import views

app_name = "welcome"
urlpatterns = [
    path("", views.welcome_view, name="welcome"),
]
