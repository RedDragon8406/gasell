# Generated by Django 3.1.2 on 2020-12-14 15:48

from django.db import migrations, models
import gasell_settings.models


class Migration(migrations.Migration):

    dependencies = [
        ('gasell_settings', '0002_sitesetting_logo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='location_image',
            field=models.ImageField(blank=True, null=True, upload_to=gasell_settings.models.upload_image_path, verbose_name='تصویر مکان'),
        ),
    ]
