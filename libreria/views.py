from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Bienvenido Keyner</h1>")
def cotizacion(request):
    return render(request, 'paginas/cotizacion.html')
def cotizaciones(request):
    return render(request, 'Cotizaciones/index.html')

def formulario(request, *args, **kwargs):
    print(request, args, kwargs)
    with open("./loger.txt", "w") as f:
        f.write("\nrequest:"+str(request)+"\nargs:"+str(args)+"\nkwargs:"+str(kwargs))
    return render(request, 'paginas/formulario_compra.html', )

def form(request):
    return render(request, 'cotizaciones/from.html')

def lavadora_lg_19_kg_42_libras_color(request):
    return render(request, 'paginas/lavadora lg 19 kg 42 libras color.html')