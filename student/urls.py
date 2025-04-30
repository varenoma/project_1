from django.urls import path

from student.views import home, student_detail

app_name = 'student'

urlpatterns = [
    path('',home,name='home'),
    path('student/<int:id>',student_detail,name='student_detail'),
]