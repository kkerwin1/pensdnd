from django.urls import path, include
from . import views

urlpatterns = [
    path('application', views.get_application),
]
