from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import NameForm


# Create your views here.

def get_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/getname/thanks/')
	else:
		form = NameForm()
		#form.fields['created_on'].widget = forms.HiddenInput()
	return render(request, 'templates/name.html', {'form': form})

class NameThanks(TemplateView):
	template_name = "templates/thanks.html"
