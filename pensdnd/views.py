from django.shortcuts import render

def index(request):
	return render(request, "static/html/index.html")

def be_a_dm(request):
	return render(request, "static/html/be_a_dm.html")
