from datetime import datetime

from faker import Faker

from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=16)  # clean phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)

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
            address=faker.address()
        )
        student.save()


class Group(models.Model):
    gr_name = models.CharField(max_length=20)
    number_of_students = models.IntegerField()
    curator = models.CharField(max_length=50)
    faculty = models.CharField(max_length=200)
    department = models.CharField(max_length=200)











