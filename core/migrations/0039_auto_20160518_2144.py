# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 21:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20160406_0104'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='ServiceSection',
        ),
        migrations.RenameModel(
            old_name='Technology',
            new_name='TechnologySection',
        ),
    ]