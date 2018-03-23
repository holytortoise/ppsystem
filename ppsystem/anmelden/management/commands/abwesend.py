from django.core.management.base import BaseCommand, CommandError
from django.db import models as m

from anmelden import models


class Command(BaseCommand):
    help = "Alle Schüler auf abwesend setzen"

    def add_arguments(self,parser):
        pass

    def handle(self, *args, **options):
        abwesend()


def abwesend():
    """
    Setzt alle Schüler auf abwesend
    """
    schülers = models.Schüler.objects.all()
    for schüler in schülers:
        schüler.anwesend = False
        schüler.save()
