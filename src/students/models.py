from datetime import datetime
import string
import random

from faker import Faker

from django.db import models


class Student(models.Model):
    GRADE_CHOICES = (
        (1, 'Junior'),
        (2, 'Middle'),
        (3, 'Senior'),
    )

    grade = models.PositiveSmallIntegerField(choices=GRADE_CHOICES)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    # add avatar TODO
    telephone = models.CharField(max_length=30, unique=True)  # clean phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)
    group_id = models.ForeignKey('students.Group',
                                 null=True, blank=True,
                                 on_delete=models.CASCADE)
    active_user = models.BooleanField(default=False)

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}'

    @classmethod
    def generate_student(cls):
        faker = Faker()

        student = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            birth_date=datetime.now().date(),
            email=faker.email(),
            telephone=faker.phone_number(),
            address=faker.address(),
        )
        student.save()
        return student

    def __str__(self):
        return f'{self.id} {self.full_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    gr_name = models.CharField(max_length=20)
    number_of_students = models.IntegerField()
    faculty = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    starosta = models.ForeignKey('students.Student',
                                 null=True, blank=True,
                                 on_delete=models.CASCADE)
    teacher = models.ForeignKey('teachers.Teacher',
                                null=True, blank=True,
                                on_delete=models.CASCADE)

    def get_info(self):
        return f'{self.gr_name}, {self.number_of_students}, {self.teacher.full_name}, {self.faculty}, {self.department}'

    def __str__(self):
        return f'{self.gr_name}'

    @classmethod
    def gen_group(cls):
        faker = Faker()
        faculty_lst = ['Faculty of Architecture and History of Art',
                       'Faculty of Philosophy',
                       'Faculty of Human, Social and Political Science',
                       'Faculty of Law',
                       'Faculty of Biology',
                       'Faculty of Economics',
                       'Institute of Criminology',
                       'Engineering',
                       'Faculty of Business and Management',
                       'Computer Science and Technology'
                       ]

        department_lst = ['Architecture',
                          'History of Art',
                          'East Asian Studies',
                          'Middle Eastern Studies',
                          'Biological Anthropology',
                          'Leverhulme Centre for Human Evolutionary Studies',
                          'Social Anthropology',
                          'Centre for Gender Studies',
                          'Lauterpacht Centre for International Law',
                          'Energy, Fluid Mechanics and Turbomachinery',
                          'Civil Engineering',
                          'Centre for Business Research',
                          'Psychometrics Centre'
                          ]

        group = cls(
            gr_name=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7)),
            number_of_students=random.randint(5, 20),
            faculty=random.choice(faculty_lst),
            department=random.choice(department_lst)
        )
        group.save()
        return group


class Logger(models.Model):
    path = models.CharField(max_length=200)
    method = models.CharField(max_length=6)
    time_delta = models.DecimalField(max_digits=5, decimal_places=3)
    user_id = models.IntegerField()
    user_email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)


from students.signals import *
