# Generated by Django 4.0.2 on 2023-06-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0059_work_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_leads',
            name='ex_duration',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='daily_leeds',
            name='ex_duration',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
