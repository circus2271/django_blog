from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def test(request):
    return HttpResponse('test works')

def index(request):
	return render(request, 'outcinema/index.html', {'data': 'foo'})

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
