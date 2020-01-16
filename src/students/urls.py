from django.urls import path
from students.views import (
    generate_student, students,
    generate_group, groups, stud_add,
    group_add, students_edit, contact, group_edit)


urlpatterns = [
    path('list/', students, name='students'),
    path('generate/', generate_student, name='generate-student'),
    path('add/', stud_add, name='students-add'),
    path('edit/<int:pk>/', students_edit, name='students-edit'),
    path('groups/', groups, name='groups'),
    path('generate-group/', generate_group, name='generate-group'),
    path('groups-add/', group_add, name='group-add'),
    path('edit-group/<int:pk>/', group_edit, name='groups-edit'),
    path('contact/', contact, name='contact'),
]
