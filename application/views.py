from django.shortcuts import render, redirect
from .forms import ApplicationForm
from django.views.generic import TemplateView
from django import forms

# Create your views here.

def get_application(request):
	if request.method == 'POST':
		form = ApplicationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/application/thanks/')
	else:
		form = ApplicationForm()
		return render(request, 'templates/application.html', {'form': form})

class ApplicationThanks(TemplateView):
	template_name = "templates/application_thanks.html"
