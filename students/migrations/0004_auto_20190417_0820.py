# Generated by Django 2.2 on 2019-04-17 02:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0003_auto_20190417_0819'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_detail',
            new_name='UserDetail',
        ),
    ]
