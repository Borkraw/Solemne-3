# Generated by Django 3.1.2 on 2020-12-13 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0003_auto_20201213_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactos',
            name='estado',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='contactos',
            name='receptor',
            field=models.CharField(default='', max_length=200),
        ),
    ]
