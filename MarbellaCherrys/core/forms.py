from django.forms import modelform_factory, inlineformset_factory
from core.models import Huerto, Plantacion

HuertoForm = modelform_factory(Huerto, fields=["nombre", "hcta_total", "nombre_ubicacion", "ubicacion"])
PlantacionFormSet = inlineformset_factory(
    Huerto, Plantacion, fields=["variedad", "hcta_total"], extra=1, can_delete=False
)