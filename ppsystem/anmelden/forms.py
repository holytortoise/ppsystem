from django import forms
from . models import Schüler,Rfid


class SuchForm(forms.Form):
    vorname = forms.CharField(max_length=50)
    nachname = forms.CharField(max_length=50)
