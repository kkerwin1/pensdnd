from django import forms
from .models import FeedbackModel

class FeedbackForm(forms.ModelForm):
	slug = forms.SlugField(widget=forms.HiddenInput(), required=False)
	class Meta:
		model = FeedbackModel
		fields = '__all__'
