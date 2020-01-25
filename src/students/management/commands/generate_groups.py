from django.core.management.base import BaseCommand

from students.models import Group, Student
from teachers.models import Teacher

import random


class Command(BaseCommand):
    help = 'Generate 100 random groups'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Enter number of groups',
        )

    def handle(self, *args, **options):
        # т.к. 1 студент может быть старостой только в одной группе, генирим студентов столько же,сколько и групп
        number = int(options.get('number') or 100)
        students = [Student.generate_student() for _ in range(number)]
        teachers = [Teacher.gen_teacher() for i in range(10)]

        for i in range(number):
            group = Group.gen_group()
            group.starosta = random.choice(students)
            group.teacher = random.choice(teachers)
            group.save()

