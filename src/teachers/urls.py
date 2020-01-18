from django.urls import path
from teachers.views import (
    generate_teacher, teachers,
    teacher_add, teacher_edit)

urlpatterns = [
    path('list/', teachers, name='teachers'),
    path('generate/', generate_teacher, name='generate-teacher'),
    path('add/', teacher_add, name='teachers-add'),
    path('edit/<int:pk>', teacher_edit, name='teacher-edit')
]
