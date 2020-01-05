from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(f'{student.get_info()}')


def students(request):
    queryset = Student.objects.all()
    response = ''

    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__contains=fn)
        # __contains --> like '%blabla%'
        # __endswith --> like '%blabla'
        # __startswith --> like 'blabla%'
        # __istarts/ends/--> регистронезависимый поиск

    for student in queryset:
        response += student.get_info() + '<br>'
    return render(request,
                  'students_list.html',
                  context={'students_list': response})

