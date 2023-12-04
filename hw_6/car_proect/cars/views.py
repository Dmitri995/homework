from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def toyota(request):
    return render(request, 'toyota.html')

def honda(request):
    return render(request, 'honda.html')

def renault(request):
    return render(request, 'renault.html')
