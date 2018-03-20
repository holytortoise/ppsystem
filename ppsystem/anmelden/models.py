from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
import datetime
# Create your models here.

class Rfid(models.Model):
    rfid_nr = models.BigIntegerField()

    def __str__(self):
        return "{}".format(self.id)


class Schüler(models.Model):
    vorname = models.CharField(max_length=50)
    nachname = models.CharField(max_length=50)
    klassenstufe = models.IntegerField()
    klassengruppe = models.CharField(max_length=1)
    rfid = models.ForeignKey(Rfid)
    anwesend = models.BooleanField(default=False)

    def __str__(self):
        return "{} {} {} {}".format(self.nachname,self.vorname,self.klassenstufe,self.klassengruppe)


class Zeit(models.Model):
    schüler = models.ForeignKey(Schüler)
    zeit = models.TimeField()
    datum = models.DateField()
