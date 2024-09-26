from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculadora/', views.calcularFemininoMasculino, name='calcularFemininoMasculino'),
    path('resultado/', views.resultadoHM, name='resultadoHM'),
]