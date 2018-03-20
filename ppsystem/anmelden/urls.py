from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'anmelden'

urlpatterns = [
    url(r'^schüler_erstellen', views.SchülerCreate.as_view(), name='schüler_create'),
    url(r'^rfid_erstellen', views.RfidCreate.as_view(), name='rfid_create'),
    url(r'^schüler_liste', views.SchülerList.as_view(), name='schüler_list'),
    url(r'^schüler_update/(?P<pk>[0-9]+)/$',
     views.SchülerUpdate.as_view(), name="schüler_update"),
    url(r'^schüler_löschen/(?P<pk>[0-9]+)/$',
      views.SchülerDelete.as_view(), name='schüler_delete'),
    url(r'^schüler_detail/(?P<pk>[0-9]+)/$',
      views.SchülerDetail.as_view(), name='schüler_detail'),
    url(r'^rfid_liste', views.RfidList.as_view(), name='rfid_list'),
    url(r'^rfid_update/(?P<pk>[0-9]+)/$',
     views.RfidUpdate.as_view(), name='rfid_update'),
    url(r'^rfid_delete/(?P<pk>[0-9]+)/$',
     views.RfidDelete.as_view(), name='rfid_delete'),
    url(r'^rfid_detail/(?P<pk>[0-9]+)/$', views.rfid_detail, name='rfid_detail'),
    url(r'^anmelden/$', views.anmelden, name="anmelden"),
]
