from django.urls import path, include
from . import views

urlpatterns = [
    path('feedback', views.get_feedback),
]
