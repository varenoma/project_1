from django.shortcuts import render, get_object_or_404
from blog.models import Blog

# Create your views here.
def home(request):
    data = Blog.objects.order_by('-yaratilgan_vaqt')[:10]
    return render(request,'blog/home.html',{'data':data})

def post_detail(request,id):
    tanla = get_object_or_404(Blog,id=id)
    return render(request,'blog/post_detail.html',{'tanla':tanla})