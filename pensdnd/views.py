from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = "static/html/index.html"

def index(request):
	return render(request, "static/html/index.html")

def be_a_dm(request):
	return render(request, "static/html/be_a_dm.html")

def main_css(request):
	return render(request, "static/css/main.css")
