# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_auto_20160518_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='logo',
            field=models.TextField(blank=True, help_text=b'SVG contents. It is recommended to use a compressor such as https://jakearchibald.github.io/svgomg/ and remove width/height attributes. It should always have a viewBox attribute.'),
        ),
    ]
