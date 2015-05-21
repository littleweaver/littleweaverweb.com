# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_simplepage_worklistpage_workpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='featured_work',
            field=models.ForeignKey(to='core.WorkPage', null=True),
            preserve_default=True,
        ),
    ]
