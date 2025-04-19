from django.forms import modelform_factory, inlineformset_factory
from core.models import Huerto, Plantacion, Insumo, Proveedor, InsumoHerreria
from django.forms.widgets import DateInput
from django import forms

HuertoForm = modelform_factory(Huerto, fields=["nombre", "hcta_total", "nombre_ubicacion", "ubicacion"])

PlantacionFormSet = inlineformset_factory(
    Huerto, Plantacion, 
    fields=["variedad", "hcta_total"], 
    extra=1,  
    can_delete=True
)

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'tipo', 'precio', 'stock', 'etiqueta', 'capacidad', 'carencia', 'proveedor']



class HerreroForm(forms.ModelForm):
    class Meta:
        model = InsumoHerreria
        fields = ['nombre', 'estado', 'operador', 'precio', 'last_use','proveedor']
        widgets = {
            'last_use': DateInput(
                attrs={
                    'type': 'date',  # Input type date para navegadores modernos
                    'class': 'form-control datepicker',
                },
                format='%Y-%m-%d'  # Formato que espera el input date
            ),
        }

