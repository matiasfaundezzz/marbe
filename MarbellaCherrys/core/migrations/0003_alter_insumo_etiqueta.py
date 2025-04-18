# Generated by Django 4.2.7 on 2025-04-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_insumo_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='etiqueta',
            field=models.CharField(choices=[('verde', 'Verde'), ('azul', 'Azul'), ('amarillo', 'Amarillo'), ('rojo', 'Rojo')], default='Verde', max_length=10),
        ),
    ]
