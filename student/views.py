from django.shortcuts import render, get_object_or_404
from student.models import Student

# Create your views here.
def home(request):
    data = Student.objects.filter(gpa__gt = 3)
    return render(request,'student/home.html',{'data':data})


def student_detail(request,id):
    data = get_object_or_404(Student, id=id)
    return render(request,'student/student_detail.html',{'data':data})