from django.shortcuts import render
from .forms import ApplicationForm
from django.views.generic import TemplateView
from django import forms

# Create your views here.

def get_application(request):
	if request.method == 'POST':
		form = ApplicationForm(request.POST)
		if form.is_valid():
			form.save()
			returnResponseRedirect('/application_thanks/')
	else:
		form = ApplicationForm()
		#form.fields['i'].widget = forms.HiddenInput()
		form.fields['tie_breaker'].widget = forms.HiddenInput()
		form.fields['slug'].widget = forms.HiddenInput()
		return render(request, 'templates/application.html', {'form': form})

class ApplicationThanks(TemplateView):
	template_name = "templates/application_thanks.html"
