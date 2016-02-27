# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_workpage_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpage',
            name='link',
            field=models.CharField(help_text=b'External URL of the project.', max_length=255, null=True, verbose_name=b'Client External URL', blank=True),
        ),
    ]
