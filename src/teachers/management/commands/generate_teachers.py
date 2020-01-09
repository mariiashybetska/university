from django.core.management.base import BaseCommand, CommandError
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate 100 random teachers'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Enter number of teachers',
        )

    def handle(self, *args, **options):
        number = int(options.get('number') or 100)
        for i in range(number):
            Teacher.gen_teacher()
