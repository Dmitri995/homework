from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, 'main.html')

def news_page(request):
    return render(request, 'news.html')

def management_page(request):
    return render(request, 'management.html')

def facts_page(request):
    return render(request, 'facts.html')

def contacts_page(request):
    return render(request, 'contacts.html')
