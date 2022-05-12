from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_application),
	path('thanks/', views.ApplicationThanks.as_view())
]
