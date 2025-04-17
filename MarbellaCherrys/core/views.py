from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from core.models import Huerto, Plantacion
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
    huertos_list = Huerto.objects.all().prefetch_related('plantaciones')

    paginator = Paginator(huertos_list, 15)
    page_number = request.GET.get('page')
    huertos = paginator.get_page(page_number)
    
    return render(request, 'core/huertos.html', {'huertos': huertos})

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


def detalle_huerto(request, huerto_id):
    huerto = get_object_or_404(Huerto.objects.prefetch_related('plantaciones'), id=huerto_id)
    return render(request, 'core/ver_huerto.html', {'huerto': huerto})

def editar_huerto(request, huerto_id):
    huerto = get_object_or_404(Huerto, id=huerto_id)
    
    if request.method == "POST":
        huerto_form = HuertoForm(request.POST, instance=huerto)
        plantacion_formset = PlantacionFormSet(request.POST, instance=huerto)
        
        if huerto_form.is_valid() and plantacion_formset.is_valid():
            huerto_form.save()
            plantacion_formset.save()
            return redirect('detalle_huerto', huerto_id=huerto.id)
    else:
        huerto_form = HuertoForm(instance=huerto)
        plantacion_formset = PlantacionFormSet(instance=huerto)
    
    return render(request, "core/editar_huerto.html", {
        "huerto": huerto,
        "huerto_form": huerto_form,
        "plantacion_formset": plantacion_formset,
    })