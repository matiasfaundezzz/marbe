from django.db import models
from django.contrib.auth.models import User
import datetime


class Maestro(models.Model):
    ESTADOS_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    TIPOS_CHOICES = [
        ('insumo', 'Insumo'),
        ('herrero', 'Herrero'),
    ]
    nombre =  models.CharField(max_length=255, null=True, blank=True)
    apellidos =  models.CharField(max_length=255, null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='maestros')
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono_contacto = models.CharField(max_length=20, null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS_CHOICES, default='Activo')
    tipo = models.CharField(max_length=10, choices=TIPOS_CHOICES, default='Herrero')

    def __str__(self):
        return self.nombre
    
class Administrador(models.Model):
    ESTADOS_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    nombre =  models.CharField(max_length=255, null=True, blank=True)
    apellidos =  models.CharField(max_length=255, null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='administrador')
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono_contacto = models.CharField(max_length=20, null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS_CHOICES, default='Activo')

    def __str__(self):
        return self.nombre

class SuperAdministrador(models.Model):
    ESTADOS_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    nombre =  models.CharField(max_length=255, null=True, blank=True)
    apellidos =  models.CharField(max_length=255, null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='superadministrador')
    estado = models.CharField(max_length=10, choices=ESTADOS_CHOICES, default='Activo')
    
    def __str__(self):
        return self.nombre
    
class Huerto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    hcta_total = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_ubicacion = models.CharField(max_length=100, null=True, blank=True)
    ubicacion = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Plantacion(models.Model):
    huerto = models.ForeignKey(Huerto, on_delete=models.CASCADE, related_name='plantaciones')
    variedad = models.CharField(max_length=255)
    hcta_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.variedad} en {self.huerto.nombre}"
    
class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    nombre_contacto = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_empresa


class Insumo(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    capacidad = models.FloatField()
    precio = models.IntegerField()
    carencia = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,related_name='proveedores')

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"

class InventarioInsumo(models.Model):
    huerto = models.ForeignKey(Huerto, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    class Meta:
        unique_together = ('huerto', 'insumo')

    def __str__(self):
        return f"{self.huerto} - {self.insumo}: {self.cantidad}"

