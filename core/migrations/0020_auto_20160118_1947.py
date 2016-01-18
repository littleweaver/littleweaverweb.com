# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20151211_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='workpage',
            name='testimonial',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='workpage',
            name='testimonial_credit',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
