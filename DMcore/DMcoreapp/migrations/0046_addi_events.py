# Generated by Django 4.0.2 on 2023-05-11 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0045_alter_events_diry_file_alter_events_fb_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='addi_events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('file', models.ImageField(blank=True, null=True, upload_to='images/smo_post/')),
                ('events', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DMcoreapp.events')),
                ('executive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DMcoreapp.user_registration')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DMcoreapp.smo_post')),
            ],
        ),
    ]