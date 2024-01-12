from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'sisamhil/home.html' context={
        'name': 'Sisamhil'
    })

def contato(request):
    return render(request, 'sisamhil/contato.html')

def sobre(request):
    return HttpResponse('SOBRE')

