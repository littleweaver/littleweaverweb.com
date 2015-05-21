# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_workpage_screenshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.WorkPage', null=True),
            preserve_default=True,
        ),
    ]
