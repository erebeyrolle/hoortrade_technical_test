from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Forms importation for the Create view
from .forms import BookCreate, AuthorCreate
# Models importation for the views
from .models import Author, Book


# Views creation below

# Test 1st URL tutorial
# def books_home(request):
#     return HttpResponse("Hello, world. You're at the Books home page.")

# Library Home Page & render
def home(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'books/index.html', {'books': books,  })

# Book Details page & render
def details(request, book_id):
    book = Book.objects.get(id = book_id)
    return render(request, 'books/details.html', {'book': book, })

# Book Create page & render
def create_book(request):
    create1 = BookCreate()
    if request.method == 'POST':
        create1 = BookCreate(request.POST, request.FILES)
        if create1.is_valid():
            create1.save()
            return redirect('home')
        else:
            return HttpResponse('Formulaire incorrect')
    else:
        return render(request, 'books/create_form.html', {'create_form': create1})

# Author Create page & render
def create_author(request):
    create2 = AuthorCreate()
    if request.method == 'POST':
        create2 = AuthorCreate(request.POST, )
        if create2.is_valid():
            create2.save()
            return redirect('home')
        else:
            return HttpResponse('Formulaire incorrect')
    else:
        return render(request, 'books/create_form.html', {'create_form': create2})

# Book Update page & render
def update_book(request, book_id):
    book = Book.objects.get(id = book_id)
    book_update = BookCreate(request.POST or None, instance = book)
    if book_update.is_valid():
        book_update.save()
        return redirect('home')
    return render(request, 'books/create_form.html', {'create_form':book_update})

# Book Delete page & render
def delete_book(request, book_id):
    book = Book.objects.get(id = book_id)
    book.delete()
    return redirect('home')