# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20160226_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpage',
            name='link',
            field=models.URLField(help_text=b'External URL of the project.', max_length=255, null=True, verbose_name=b'Client External URL', blank=True),
        ),
    ]
