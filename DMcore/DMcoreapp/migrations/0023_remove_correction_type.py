# Generated by Django 4.0.2 on 2023-04-24 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0022_correction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correction',
            name='type',
        ),
    ]