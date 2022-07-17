from django.urls import path

from AppFamilia.views import Inicio, Padres, Hermanos

urlpatterns = [
    path('', Inicio),
    path('padres/',Padres),
    path('hermanos/', Hermanos),
]
