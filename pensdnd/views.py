from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = "static/html/index.html"

class BeADM(TemplateView):
	template_name = "static/html/be_a_dm.html"
