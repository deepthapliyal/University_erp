# students/views.py
from django.shortcuts import render, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, roll_number):
    student = get_object_or_404(Student, roll_number=roll_number)
    return render(request, 'students/student_detail.html', {'student': student})
