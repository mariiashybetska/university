from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth import login, authenticate, logout

from students.models import Student, Group
from students.forms import (StudentsAddForm, GroupsAddForm, ContactForm, RegistrationForm,
                            UserRegistrationForm, UserLoginForm)


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(f'{student.get_info()}')


def students(request):
    queryset = Student.objects.all().select_related('group_id')  # указываем название внешнего ключа
    # response = ''

    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__contains=fn)
        # __contains --> like '%blabla%'
        # __endswith --> like '%blabla'
        # __startswith --> like 'blabla%'
        # __istarts/ends/--> регистронезависимый поиск

    # for student in queryset:
    #     response += student.get_info() + '<br>'
    return render(request,
                  'students_list.html',
                  context={'students': queryset})


def generate_group(request):
    group = Group.gen_group()
    return HttpResponse(f'{group.get_info()}')


def groups(request):
    queryset = Group.objects.all().select_related('starosta', 'teacher')

    # response = ''

    f = request.GET.get('faculty')
    if f:
        queryset = queryset.filter(faculty__contains=f)

    # for group in queryset:
    #     response += group.get_info() + '<br>'

    return render(request,
                  'groups_list.html',
                  context={'groups': queryset})


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
            return HttpResponseRedirect(reverse('groups'))
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
            with open('log.txt', 'a') as f:
                for key, value in form.cleaned_data.items():
                    f.write(f'{key}:{value}\n')
            form.save()
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = ContactForm()

    return render(request,
                  'contact.html',
                  context={'form': form})


def group_edit(request, pk):
    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return HttpResponseNotFound(f'Group whit id {pk} is not found')

    if request.method == 'POST':
        form = GroupsAddForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm(instance=group)

    return render(request,
                  'group_edit.html',
                  context={'form': form, 'pk': pk})


def reg_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('registration'))
    else:
        form = RegistrationForm()

    return render(request,
                  'registration.html',
                  context={'form': form})


def activate_user(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Student whit id {pk} is not found')

    student.active_user = True
    student.save()
    return render(request,
                  'activate_user.html',
                  context={'student': student})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reg'))
    else:
        form = UserRegistrationForm()

    return render(request,
                  'register.html',
                  context={'form': form})


def custom_login(request):
    user_form = UserLoginForm

    if request.GET.get('logout'):
        logout(request)

    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],
                                )
            login(request, user)

            return HttpResponseRedirect(reverse('students'))
    else:
        form = user_form()

    return render(request,
                  'login.html',
                  context={'form': form})



