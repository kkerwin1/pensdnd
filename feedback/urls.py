from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_feedback),
	path('feedback_thanks/', views.FeedbackThanks.as_view())
]
