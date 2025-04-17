
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("huertos/", views.huertos, name="huertos"),
    path("agregar_huertos/", views.huerto_list_create, name="agregar_huertos"),
    path('huertos/<int:huerto_id>/', views.detalle_huerto, name='detalle_huerto'),
    path('huertos/editar/<int:huerto_id>/', views.editar_huerto, name='editar_huerto'),
    path("maestroinsumo/", views.maestroinsumo, name="maestroinsumo"),
    path("maestroherrero/", views.maestroherrero, name="maestroherrero"),
    path("inventario/", views.inventario, name="inventario"),
    path("proveedores/", views.proveedores, name="proveedores"),

]


