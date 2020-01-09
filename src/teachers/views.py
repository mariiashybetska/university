from teachers.models import Teacher

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q


def generate_teacher(request):
    teacher = Teacher.gen_teacher()
    return HttpResponse(f'{teacher.get_info()}')


def teachers(request):
    queryset = Teacher.objects.all()
    response = ''

    fltr = request.GET.get('filter')
    if fltr:
        queryset = queryset.filter(
            Q(first_name__contains=fltr) | Q(last_name__contains=fltr) | Q(email__contains=fltr)
        )

    for teacher in queryset:
        response += teacher.get_info() + '<br>'

    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})
