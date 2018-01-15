from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$', views.home, name='home'),
    url(r'^home', views.home, name='home'),
    url(r'^guide', views.guide, name='guide'),
    url(r'^contact',views.contact, name='contact'),
    url(r'^BOP',views.Bop, name='BOP'),
    url(r'^PLSA',views.Plsa, name='PLSA'),
    url(r'^resultTemp',views.resultTemp, name='resultTemp'),
    url(r'^result',views.result, name='result'),
    url(r'^resultPLSA',views.resultPLSA, name='resultPLSA'),
    url(r'^invalid',views.invalid, name='invalid'),
]