# Generated by Django 3.2.19 on 2023-07-07 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0002_auto_20230706_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_leeds_exists',
            name='date',
            field=models.DateField(default=datetime.date(2023, 7, 7)),
        ),
    ]
