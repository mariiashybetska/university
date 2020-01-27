from django.urls import path
from students.views import (
    generate_student, students,
    generate_group, groups, stud_add,
    group_add, students_edit, contact,
    group_edit)


urlpatterns = [
    path('generate/', generate_student, name='generate-student'),
    path('list/', students, name='students'),
    path('generate-group/', generate_group, name='generate-group'),
    path('groups/', groups, name='groups'),
    path('add/', stud_add, name='students-add'),
    path('groups-add/', group_add, name='groups-add'),
    path('edit/<int:pk>/', students_edit, name='students-edit'),
    path('contact/', contact, name='contact'),
    path('groups/edit/<int:pk>/', group_edit, name='group-edit')
]
