# Generated by Django 2.0.2 on 2022-03-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('piso', models.AutoField(primary_key=True, serialize=False)),
                ('tipo1', models.CharField(choices=[('Vip', 'Vip'), ('C', 'Colaborador'), ('V', 'Visita')], max_length=3)),
                ('telefono', models.CharField(max_length=9)),
            ],
        ),
    ]
