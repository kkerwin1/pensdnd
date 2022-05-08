from django.shortcuts import render
from .forms import ApplicationForm

# Create your views here.

def get_application(request):
	if request.method is 'POST':
		form = ApplicationForm(request.POST)
		if form.is_valid():
			returnResponseRedirect('/thanks_application/')
	else:
		form = ApplicationForm()
	return render(request, 'application.html', {'form': form})
