from django.shortcuts import render

# Create your views here.
from .models import Genre, Book

def home(request):
    genre = Genre.objects.get(id=2)
    books = Book.objects.all()
    context = {
        "books": books,
        "janr": genre
    }

    return render(request, "home.html", context)