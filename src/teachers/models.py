from datetime import datetime
import random

from faker import Faker

from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=30)  # clean phone TODO
    faculty = models.CharField(max_length=255)

    def get_info(self):
        return f'{self.first_name} {self.last_name}, {self.birth_date}, {self.email}, {self.telephone}, {self.faculty}'

    @classmethod
    def gen_teacher(cls):
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
        teacher = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            birth_date=datetime.now().date(),
            email=faker.email(),
            telephone=faker.phone_number(),
            faculty=random.choice(faculty_lst)
        )
        teacher.save()
        return teacher
