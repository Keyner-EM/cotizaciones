from django.urls import path
from . import views

urlpatterns = [
    path('cotizaciones', views.cotizaciones, name='cotizaciones'),
    path('formulario', views.formulario, name='formulario'),
    path('lavadora lg 19 kg 42 libras color', views.lavadora_lg_19_kg_42_libras_color, name='lavadora'),
    path('Lavadora Mabe 16kg 35 libras color gris', views.Lavadora_Mabe_16kg_35_libras_color_gris, name='Lavadora Mabe 16kg 35 libras color gris'),
    path('Equipo LG', views.Equipo_LG, name='Equipo LG'),
    path('Estufa 51cm', views.Estufa_51cm, name='Estufa'),
    path('Estufa mabe 51cm', views.Estufa_mabe_51cm, name='Estufa mabe 51cm'),
    path('Nevecon Lg 508 lts no frost', views.Nevecon_Lg_508_lts_no_frost, name='Nevecon Lg 508 lts no frost'),
    path('Nevera Challenger 317 lts no frost', views.Nevera_Challenger_317_lts_no_frost, name='Nevera Challenger 317 lts no frost'),
    path('Nevera Mabe RMP405FYCU', views.Nevera_Mabe_RMP405FYCU, name='Nevera Mabe RMP405FYCU'),
    path('Televisor LG 32', views.Televisor_LG_32, name='Televisor LG 32'),
    path('Televisor LG 50', views.Televisor_LG_50, name='Televisor LG 50'),
]