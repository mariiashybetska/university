from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from students.models import Student, Group
from students.forms import StudentsAddForm, GroupsAddForm, ContactForm


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


def generate_group(request):
    group = Group.gen_group()
    return HttpResponse(f'{group.get_info()}')


def groups(request):
    queryset = Group.objects.all()
    response = ''

    fn = request.GET.get('faculty')
    if fn:
        queryset = queryset.filter(faculty__contains=fn)

    for group in queryset:
        response += group.get_info() + '<br>'

    return render(request,
                  'groups_list.html',
                  context={'groups_list': response})


def stud_add(request):
    if request.method == 'POST':
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm()

    return render(request,
                  'student_add.html',
                  context={'form': form})


def group_add(request):
    if request.method == 'POST':
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')
    else:
        form = GroupsAddForm()

    return render(request,
                  'group_add.html',
                  context={'form': form})


def students_edit(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Student whit id {pk} is not found')

    if request.method == 'POST':
        form = StudentsAddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm(instance=student)

    return render(request,
                  'student_edit.html',
                  context={'form': form, 'pk': pk})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = ContactForm()

    return render(request,
                  'contact.html',
                  context={'form': form})
