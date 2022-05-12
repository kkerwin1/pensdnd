from django import forms
from .models import NameModel

class NameForm(forms.ModelForm):
	class Meta:
		model = NameModel
		fields = '__all__'
