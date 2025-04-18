from django.forms import modelform_factory, inlineformset_factory
from core.models import Huerto, Plantacion, Insumo, Proveedor
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
        fields = ['codigo', 'nombre', 'tipo', 'precio', 'stock', 'etiqueta', 'capacidad', 'carencia', 'proveedor']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if Insumo.objects.filter(codigo=codigo).exclude(id=self.instance.id if self.instance else None).exists():
            raise forms.ValidationError("Este código ya está en uso.")
        return codigo
