from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Film, HomepageSlider

def test(request):
    return HttpResponse('test works')

def index(request):
	films = Film.objects.all()
	slider = HomepageSlider.objects.all()[0]
	return render(request, 'outcinema/index.html', {'data': 'foo', 'films': films, 'slider': slider})

def films(request):
	return render(request, 'outcinema/films.html')

def events(request):
	return render(request, 'outcinema/events.html')

def rent(request):
	return render(request, 'outcinema/rent.html')

def about(request):
	return render(request, 'outcinema/about.html')

def faq(request):
	return render(request, 'outcinema/faq.html')
