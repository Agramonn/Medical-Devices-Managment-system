# Generated by Django 4.2.4 on 2023-09-25 03:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0039_reporteusuario_orden_delete_cama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='desempeño_general',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='num_contrato',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='equipo_medico',
            name='numero_nacional_inv',
            field=models.CharField(max_length=100, unique=True),
        ),

    ]
