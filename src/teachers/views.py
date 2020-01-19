from teachers.models import Teacher
from teachers.forms import TeachersAddForm

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound
from django.db.models import Q
from django.urls import reverse


def generate_teacher(request):
    teacher = Teacher.gen_teacher()
    return HttpResponse(f'{teacher.get_info()}')


def teachers(request):
    queryset = Teacher.objects.all()
    # response = ''

    fltr = request.GET.get('filter')
    if fltr:
        queryset = queryset.filter(
            Q(first_name__contains=fltr) | Q(last_name__contains=fltr) | Q(email__contains=fltr)
        )

    # for teacher in queryset:
    #     response += teacher.get_info() + '<br>'

    return render(request,
                  'teachers_list.html',
                  context={'teachers': queryset})


def teacher_add(request):
    if request.method == 'POST':
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeachersAddForm()

    return render(request,
                  'teacher_add.html',
                  context={'form': form})


def teacher_edit(request, pk):
    try:
        teacher = Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        return HttpResponseNotFound(f'Teacher whit id {pk} is not found')

    if request.method == 'POST':
        form = TeachersAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeachersAddForm(instance=teacher)

    return render(request,
                  'teacher_edit.html',
                  context={'form': form, 'pk': pk})