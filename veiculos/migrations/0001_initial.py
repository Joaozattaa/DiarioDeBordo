# Generated by Django 5.1.3 on 2024-12-03 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('placa', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroUso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=255)),
                ('kilometragem_saida', models.IntegerField()),
                ('kilometragem_chegada', models.IntegerField(blank=True, null=True)),
                ('horario_saida', models.DateTimeField()),
                ('horario_chegada', models.DateTimeField(blank=True, null=True)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculos.veiculo')),
            ],
        ),
    ]
