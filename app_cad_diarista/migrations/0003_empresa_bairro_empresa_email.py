# Generated by Django 5.0.4 on 2024-04-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_diarista', '0002_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='bairro',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
