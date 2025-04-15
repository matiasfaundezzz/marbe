
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("huertos/", views.huertos, name="huertos"),
    path("agregar_huertos/", views.huerto_list_create, name="agregar_huertos"),
    path("maestroinsumo/", views.maestroinsumo, name="maestroinsumo"),
    path("maestroherrero/", views.maestroherrero, name="maestroherrero"),
    path("inventario/", views.inventario, name="inventario"),
    path("proveedores/", views.proveedores, name="proveedores"),
]


