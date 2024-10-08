# Generated by Django 5.0.4 on 2024-04-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diarista',
            fields=[
                ('id_diarista', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('setor', models.PositiveIntegerField()),
                ('rg', models.CharField(max_length=9)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(default='', max_length=254)),
                ('telefone', models.CharField(max_length=11)),
                ('pix', models.TextField()),
            ],
        ),
    ]
