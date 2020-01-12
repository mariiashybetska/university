
from django.contrib import admin
from django.urls import path
from students.views import (
    generate_student, students,
    generate_group, groups, stud_add,
    group_add, students_edit, contact)


urlpatterns = [
    path('generate/', generate_student),
    path('list/', students, name='students'),
    path('generate-group/', generate_group),
    path('groups/', groups),
    path('add/', stud_add, name='students-add'),
    path('groups/add/', group_add),
    path('edit/<int:pk>/', students_edit, name='students-edit'),
    path('contact/', contact, name='contact'),
]
