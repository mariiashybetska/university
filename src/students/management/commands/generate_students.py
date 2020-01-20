from django.core.management.base import BaseCommand, CommandError

from students.models import Student, Group

import random


class Command(BaseCommand):
    help = 'Generate 100 random students'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Enter number of students',
        )

    def handle(self, *args, **options):
        Group.objects.all().delete()  # truncate table
        Student.objects.all().delete()

        groups = [Group.gen_group() for i in range(10)]

        number = int(options.get('number') or 100)

        for i in range(number):
            student = Student.generate_student()
            student.group = random.choice(groups)
            student.save()

# python manage.py --number 1
