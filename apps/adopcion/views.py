from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_adopcion(request):
	return HttpResponse("<h1>Soy la pagina principal de la pagina adopción</h1>")
