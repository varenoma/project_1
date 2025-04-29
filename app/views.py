from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'app/home.html')

