from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
# Create your views here.
def index(request):
    return render(request, 'index.html')

class SchülerList(LoginRequiredMixin,ListView):
    login_url = 'account:login'
    redirect_field_name = 'redirect_to'
    queryset = models.Schüler.objects.order_by('klassenstufe','klassengruppe','nachname','vorname')
    context_object_name = 'schülers'
    template_name = 'anmelden/schüler_liste.html'


class SchülerCreate(LoginRequiredMixin,CreateView):
    login_url = 'account:login'
    redirect_field_name = 'redirect_to'
    model = models.Schüler
    fields = ['vorname','nachname','klassenstufe','klassengruppe','rfid']
    template_name = 'anmelden/schüler_erstellen.html'
    success_url = '/'

class SchülerDetail(LoginRequiredMixin,DetailView):
    login_url = 'account:login'
    redirect_field_name = 'redirect_to'
    model = models.Schüler
    context_object_name = 'schüler'
    template_name = 'anmelden/schüler_detail.html'


class SchülerUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'account:login'
    redirect_field_name = 'redirect_to'
    model = models.Schüler
    fields = ['vorname','nachname','klassenstufe','klassengruppe','rfid']
    success_url = '/'


class SchülerDelete(LoginRequiredMixin,DeleteView):
    login_url = 'account:login'
    redirect_field_name = 'redirect_to'
    model = models.Schüler
    success_url = reverse_lazy('index')
    template_name = "anmelden/schüler_löschen.html"


class RfidCreate(LoginRequiredMixin,CreateView):
    login_url = 'account:login'
    redirect_field_name = 'redirect_to'
    model = models.Rfid
    fields = ['rfid_nr']
    template_name = 'anmelden/rfid_erstellen.html'
    success_url = '/'


class RfidUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'account:login'
    redirect_field_name = 'redirect_to'
    model = models.Rfid
    fields = ['rfid_nr']
    template_name = 'anmelden/rfid_update.html'
    success_url = '/'


class RfidDelete(LoginRequiredMixin,DeleteView):
    login_url = 'account:login'
    redirect_field_name = 'redirect_to'
    model = models.Rfid
    success_url = reverse_lazy('index')
    template_name = "anmelden/rfid_löschen.html"


class RfidList(LoginRequiredMixin,ListView):
    login_url = 'account:login'
    redirect_field_name = 'redirect_to'
    queryset = models.Rfid.objects.order_by('id')
    context_object_name = 'rfids'
    template_name = 'anmelden/rfid_liste.html'

@login_required(login_url='account:login')
def rfid_detail(request,pk):
    rfid_karte = models.Rfid.objects.get(id=pk)
    schüler = models.Schüler.objects.filter(rfid=rfid_karte)
    if not schüler.exists():
        schüler = None
    context_dict = {'rfid_karte':rfid_karte,'schüler':schüler}
    return render(request,'anmelden/rfid_detail.html',context_dict)

@csrf_exempt
def anmelden(request):
    if request.method == "POST":
        UID = request.POST['UID']
        rfid = models.Rfid.objects.filter(rfid_nr=UID)
        schüler = models.Schüler.objects.get(rfid = rfid[0])
        if models.Zeit.objects.filter(schüler=schüler, datum=timezone.localdate()):
            return HttpResponse('{} {} bereits angemeldet'.format(schüler.vorname,schüler.nachname))
        zeit = models.Zeit()
        zeit.schüler = schüler
        zeit.datum = timezone.localdate()
        zeit.zeit = timezone.localtime()
        zeit.save()
        name ="{} {}".format(schüler.vorname, schüler.nachname)
        return HttpResponse(name)
    else:
        return HttpResponse('Access Denied')
