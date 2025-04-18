
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("huertos/", views.huertos, name="huertos"),
    path("agregar_huertos/", views.huerto_list_create, name="agregar_huertos"),
    path('huertos/<int:huerto_id>/', views.detalle_huerto, name='detalle_huerto'),
    path('huertos/editar/<int:huerto_id>/', views.editar_huerto, name='editar_huerto'),
    path('huertos/eliminar/<int:huerto_id>/', views.eliminar_huerto, name='eliminar_huerto'),
    path("maestroinsumo/", views.maestroinsumo, name="maestroinsumo"),
    path("maestroherrero/", views.maestroherrero, name="maestroherrero"),
    path('insumos/', views.InsumoListView.as_view(), name='insumos'),
    path('insumo/nuevo/', views.crear_insumo, name='crear_insumo'),
    path('insumo/editar/<int:insumo_id>/', views.editar_insumo, name='editar_insumo'),
    path('insumo/eliminar/<int:insumo_id>/', views.eliminar_insumo, name='eliminar_insumo'),
    path("proveedores/", views.proveedores, name="proveedores"),

]


