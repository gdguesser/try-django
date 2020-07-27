from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_context= {
		"my_text": "this is about us",
		"my_number": 996652279,
		"my_list": [123, 321, "eae"]
	}
	return render(request, "about.html", my_context)

def index(request):
	return render(request, 'index.html', {})