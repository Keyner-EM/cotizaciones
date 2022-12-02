from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def cotizaciones(request):
    if request.method == 'GET':
        cotizaciones = models.cotizacines.objects.all()
        id = request.GET.get("id")
        if id:
            cotizaciones.filter(id=id).delete()
        return render(request, 'Cotizaciones/index.html', {"cotizaciones": cotizaciones})

def formulario(request):
    if request.method == 'GET':
        return render(request, 'paginas/formulario_compra.html')
    elif request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        models.cotizacines(**data).save()
        return HttpResponse(status = 200)
        
def lavadora_lg_19_kg_42_libras_color(request):
    if request.method == 'GET':
        return render(request, 'paginas/lavadora lg 19 kg 42 libras color.html')
    elif request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        models.cotizacines(**data).save()
        return HttpResponse(status = 200)
    
def Lavadora_Mabe_16kg_35_libras_color_gris(request):
    if request.method == 'GET':
        return render(request, 'paginas/Lavadora Mabe 16kg 35 libras color gris.html')
    elif request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        models.cotizacines(**data).save()
        return HttpResponse(status = 200)
    
def Equipo_LG(request):
    if request.method == 'GET':
        return render(request, 'paginas/Equipo LG.html')
    elif request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        models.cotizacines(**data).save()
        return HttpResponse(status = 200)
    
def Estufa_51cm(request):
    if request.method == 'GET':
        return render(request, 'paginas/Estufa 51cm.html')
    elif request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        models.cotizacines(**data).save()
        return HttpResponse(status = 200)
    
def Estufa_mabe_51cm(request):
    if request.method == 'GET':
        return render(request, 'paginas/Estufa mabe 51cm.html')
    elif request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        models.cotizacines(**data).save()
        return HttpResponse(status = 200)
    
def Estufa_mabe_51cm(request):
    if request.method == 'GET':
        return render(request, 'paginas/Estufa mabe 51cm.html')
    elif request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        models.cotizacines(**data).save()
        return HttpResponse(status = 200)

def Nevecon_Lg_508_lts_no_frost(request):
    if request.method == 'GET':
        return render(request, 'paginas/Nevecon Lg 508 lts no frost.html')
    elif request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        models.cotizacines(**data).save()
        return HttpResponse(status = 200)
    
    
def Nevera_Challenger_317_lts_no_frost(request):
    if request.method == 'GET':
        return render(request, 'paginas/Nevera Challenger 317 lts no frost.html')
    elif request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        models.cotizacines(**data).save()
        return HttpResponse(status = 200)
    


def Nevera_Mabe_RMP405FYCU(request):
    if request.method == 'GET':
        return render(request, 'paginas/Nevera Mabe RMP405FYCU.html')
    elif request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        models.cotizacines(**data).save()
        return HttpResponse(status = 200)
    
    
def Televisor_LG_32(request):
    if request.method == 'GET':
        return render(request, 'paginas/Televisor LG 32.html')
    elif request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        models.cotizacines(**data).save()
        return HttpResponse(status = 200)


def Televisor_LG_50(request):
    if request.method == 'GET':
        return render(request, 'paginas/Televisor LG 50.html')
    elif request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        models.cotizacines(**data).save()
        return HttpResponse(status = 200)
    
    
