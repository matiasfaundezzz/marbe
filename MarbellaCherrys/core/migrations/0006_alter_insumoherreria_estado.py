# Generated by Django 4.2.7 on 2025-04-19 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_insumo_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumoherreria',
            name='estado',
            field=models.CharField(choices=[('operativo', 'Operativo'), ('intivo', 'Inoperativo')], default='Operativo', max_length=10),
        ),
    ]
