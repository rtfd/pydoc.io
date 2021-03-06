# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-27 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170406_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='release',
            options={'get_latest_by': 'distributions__uploaded_at', 'ordering': ['-distributions__uploaded_at'], 'verbose_name': 'release', 'verbose_name_plural': 'releases'},
        ),
        migrations.AlterField(
            model_name='distribution',
            name='filetype',
            field=models.CharField(choices=[('sdist', 'Source'), ('bdist_wheel', 'Wheel'), ('bdist_dumb', '"dumb" binary'), ('bdist_rpm', 'RPM'), ('bdist_wininst', 'MS Windows installer'), ('bdist_egg', 'Python Egg'), ('bdist_dmg', 'OS X Disk Image')], max_length=32),
        ),
    ]
