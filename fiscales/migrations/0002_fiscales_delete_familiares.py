# Generated by Django 4.1 on 2022-09-15 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiscales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fiscales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_suc', models.CharField(max_length=50)),
                ('nro_suc', models.IntegerField()),
                ('modelo_fiscal', models.CharField(max_length=40)),
                ('punto_venta', models.IntegerField()),
                ('nro_serie', models.IntegerField()),
                ('fecha_cambio', models.DateField()),
                ('estado', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Familiares',
        ),
    ]
