from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cotizacion', views.cotizacion, name='cotizaciones'),
    path('cotizaciones', views.cotizaciones, name='cotizaciones'),
    path('formulario', views.formulario, name='formulario'),
    path('form', views.form, name='form'),
    path('lavadora lg 19 kg 42 libras color', views.lavadora_lg_19_kg_42_libras_color, name='lavadora')
]