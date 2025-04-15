from django.contrib import admin
from .models import Huerto, SuperAdministrador, Administrador, Plantacion, Insumo, Maestro, Proveedor
# Register your models here.


admin.site.register(Huerto)
admin.site.register(SuperAdministrador)
admin.site.register(Administrador)
admin.site.register(Plantacion)
admin.site.register(Insumo)
admin.site.register(Maestro)
admin.site.register(Proveedor)

