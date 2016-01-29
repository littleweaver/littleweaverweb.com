# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20160129_2219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='service',
            name='sort_order',
            field=models.IntegerField(null=True, editable=False, blank=True),
        ),
    ]
