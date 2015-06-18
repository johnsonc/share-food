__author__ = 'darek'
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

TIME_WINDOW = 7


class Command(BaseCommand):


    def handle(self, *args, **options):
        pass