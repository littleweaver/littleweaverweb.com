# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20151124_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorprofile',
            name='twitter_username',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
