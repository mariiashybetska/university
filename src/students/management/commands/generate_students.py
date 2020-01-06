from django.core.management.base import BaseCommand, CommandError
from students.models import Student


class Command(BaseCommand):
    help = 'Generate 100 random students'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Enter number of students',
        )

    def handle(self, *args, **options):
        number = int(options.get('number') or 100)
        for i in range(number):
            Student.generate_student()

# python manage.py --number 1
