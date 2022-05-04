from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.

def get_feedback(request):
	if request.method is 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			returnResponseRedirect('/thanks/')
	else:
		form = FeedbackForm()
	return render(request, 'feedback.html', {'form': form})
