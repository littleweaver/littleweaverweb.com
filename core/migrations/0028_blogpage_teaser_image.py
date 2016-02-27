# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('core', '0027_auto_20160226_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='teaser_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', help_text=b'Image to display on the blog index page', null=True),
        ),
    ]
