from django.shortcuts import get_object_or_404, render
from .models import Book

# Create your views here.
def show_books(request):
    data = Book.objects.all()
    return render(request,'book/home.html',{'data': data})


def book_detail(request, id):
    kitob = get_object_or_404(Book,id=id)
    return render(request, 'book/book_detail.html',{'kitob': kitob})

