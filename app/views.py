from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'app/home.html')


def app_to_book(request):
    return redirect(reverse('show_books'))
