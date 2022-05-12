from django import forms
from .models import ApplicationModel

class ApplicationForm(forms.ModelForm):
	class Meta:
		model = ApplicationModel
		fields = '__all__'
		#ordering = ['-created_on']
		#abstract = False
		#swapped = False
		#app_label = "application"
		#get_latest_by = ['-created_on']
