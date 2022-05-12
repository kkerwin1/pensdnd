from django.shortcuts import render
from .forms import FeedbackForm
from django.views.generic import TemplateView
from django import forms

# Create your views here.

def get_feedback(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			returnResponseRedirect('/feedback_thanks')
	else:
		form = FeedbackForm()
		#form.fields['created_on'].widget = forms.HiddenInput()
	return render(request, 'templates/feedback.html', {'form': form})

class FeedbackThanks(TemplateView):
	template_name = "templates/feedback_thanks.html"
