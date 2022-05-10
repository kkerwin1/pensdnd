from django.urls import path, include
from . import views

urlpatterns = [
    path('application', views.get_application),
	path('application_thanks', views.ApplicationThanks.as_view())
]
