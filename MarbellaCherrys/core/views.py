from django.shortcuts import render, redirect
from core.models import Huerto
from .forms import HuertoForm, PlantacionFormSet

def index(request):
    return render(request, 'core/index.html')

def maestroinsumo(request):
    return render(request, 'core/minsumo.html')

def maestroherrero(request):
    return render(request, 'core/mherrero.html')

def inventario(request):
    return render(request, 'core/inventario.html')

def proveedores(request):
    return render(request, 'core/proveedores.html')

def huertos(request):
    huertos = Huerto.objects.all()
    return render(request, 'core/huertos.html' , {'huertos': huertos})

def huerto_list_create(request):
    huertos = Huerto.objects.prefetch_related('plantaciones').all()

    if request.method == "POST":
        huerto_form = HuertoForm(request.POST)
        if huerto_form.is_valid():
            nuevo_huerto = huerto_form.save()
            plantacion_formset = PlantacionFormSet(request.POST, instance=nuevo_huerto)
            if plantacion_formset.is_valid():
                plantacion_formset.save()
                return redirect("huertos")
    else:
        huerto_form = HuertoForm()
        plantacion_formset = PlantacionFormSet()

    return render(request, "core/agregar_huerto.html", {
        "huertos": huertos,
        "huerto_form": huerto_form,
        "plantacion_formset": plantacion_formset,
    })