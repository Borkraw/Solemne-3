# Generated by Django 3.1.2 on 2020-12-13 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0005_auto_20201213_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactos',
            name='receptor',
        ),
    ]
