from django.urls import path

from book.views import book_detail, show_books

app_name = 'book'

urlpatterns = [
    path('', show_books, name='book_show_books'),
    path('kitob/<int:id>', book_detail, name='book_detail'),
]