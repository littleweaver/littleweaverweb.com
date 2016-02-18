# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('core', '0024_auto_20160129_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='workpage',
            name='background_photo',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', help_text=b'Background image for homepage stripe. Should be blurred or low entropy for light text to be legible on it.', null=True),
        ),
        migrations.AlterField(
            model_name='workpage',
            name='screenshot',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
    ]
