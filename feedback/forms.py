from django import forms
from .models import FeedbackModel

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = FeedbackModel
		exclude = ['slug', 'created_on']
