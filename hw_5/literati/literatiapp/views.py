from django.shortcuts import render, redirect

# Create your views here.


def main_page(request):
    return render(request, 'main.html')

def literati_page(request):
    return render(request, 'literati.html')

def books_page(request):
    return render(request, 'books.html')

def book_page(request, num_book):
    if num_book == 1:
        return render(request, 'book1.html')
    elif num_book == 2:
        return render(request, 'book2.html')
    elif num_book == 3:
        return render(request, 'book3.html')
    else:
        return redirect('/books/')
