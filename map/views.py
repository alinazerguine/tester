from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def usa(request):
	return render(request, 'usa.html')

def nebraska(request):	
	return render(request, 'nebraska.html')