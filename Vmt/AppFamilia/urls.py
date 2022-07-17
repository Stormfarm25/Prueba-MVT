from django.urls import path

from AppFamilia.views import Inicio, Padres

urlpatterns = [
    path('', Inicio),
    path('padres.html/',Padres),
]
