# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20151208_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorprofile',
            name='bio',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
