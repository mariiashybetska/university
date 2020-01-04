from django.shortcuts import render
from django.http import HttpResponse
from students.models import *


def generate_student(request):
    Student.generate_student()
    return HttpResponse('student')
