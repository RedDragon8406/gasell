# Generated by Django 3.1.2 on 2020-12-14 09:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gasell_account', '0003_auto_20201213_2252'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileUser',
            new_name='Profile',
        ),
    ]
