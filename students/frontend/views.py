from django.shortcuts import render, redirect
from student_registration.models import Student

def student_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        roll = request.POST['roll']
        address = request.POST['address']
        Student.objects.create(name=name, age=age, roll=roll, address=address)
        return redirect('student_form')
    
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})