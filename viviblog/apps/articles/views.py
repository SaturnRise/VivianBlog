from django.http import HttpResponse

def index(request):    
	return HttpResponse("Привет, человек!")

def test(request):
	return HttpResponse ("тестовая страница")

# Create your views here.
