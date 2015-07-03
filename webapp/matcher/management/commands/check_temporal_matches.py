__author__ = 'piotr'
from django.core.management.base import BaseCommand, CommandError
from matcher import check_temporal_matches, find_temporal_matches_to_check
import datetime
import logging


class Command(BaseCommand):

    def check_temporal_matches(self):

        find_temporal_matches_to_check()
