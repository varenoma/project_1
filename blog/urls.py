from django.urls import path

from blog.views import home, post_detail

app_name = 'blog'

urlpatterns = [
    path('',home,name='home'),
    path('post/<int:id>',post_detail,name='post_detail')
]