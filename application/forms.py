from django import forms
from .models import ApplicationModel

class ApplicationForm(forms.ModelForm):
	class Meta:
		model = ApplicationModel
		exclude = ['slug', 'created_on']
