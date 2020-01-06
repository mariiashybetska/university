from django.core.management.base import BaseCommand
from students.models import Group


class Command(BaseCommand):
    help = 'Generate 100 random groups'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Enter number of groups',
        )

    def handle(self, *args, **options):
        number = int(options.get('number') or 100)
        for i in range(number):
            Group.gen_group()
