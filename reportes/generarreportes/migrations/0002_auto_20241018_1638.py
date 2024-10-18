# Generated by Django 3.2.6 on 2024-10-18 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generarreportes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cronograma',
            name='anio',
            field=models.IntegerField(default=2024),
        ),
        migrations.AddField(
            model_name='descuento',
            name='fechaFinal',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='descuento',
            name='fechaInicio',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='descuento',
            name='porcentaje',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='codigo',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pago',
            name='fecha',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='pago',
            name='interes',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pago',
            name='pagado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pago',
            name='periodicidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pago',
            name='valor',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='recibo',
            name='fecha',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='recibo',
            name='valor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pago',
            name='descuento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='generarreportes.descuento'),
        ),
    ]
