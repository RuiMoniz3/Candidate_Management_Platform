# Generated by Django 5.0.7 on 2024-07-17 22:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telemovel', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recrutador',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telemovel', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_publicacao', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.cliente')),
                ('recrutador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.recrutador')),
            ],
        ),
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_candidatura', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('em_processo', 'Em Processo'), ('desqualificado', 'Desqualificado'), ('desistiu', 'Desistiu'), ('contratado', 'Contratado')], default='em_processo', max_length=15)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.candidato')),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.vaga')),
            ],
        ),
    ]