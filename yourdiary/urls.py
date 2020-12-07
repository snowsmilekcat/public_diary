from django.urls import path
from . import views

app_name = 'yourdiary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]