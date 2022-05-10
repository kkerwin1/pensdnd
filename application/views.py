from django.shortcuts import render
from .forms import ApplicationForm
from django.views.generic import TemplateView

# Create your views here.

def get_application(request):
	if request.method is 'POST':
		form = ApplicationForm(request.POST)
		if form.is_valid():
			returnResponseRedirect('/application_thanks')
	else:
		form = ApplicationForm()
	return render(request, 'templates/application.html', {'form': form})

class ApplicationThanks(TemplateView):
	template_name = "templates/application_thanks.html"
