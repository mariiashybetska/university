from django.core.management.base import BaseCommand, CommandError
from students.models import *


class Command(BaseCommand):
    help = 'Generate 100 random students'

    def handle(self, *args, **options):
        for i in range(100):
            Student.generate_student()

