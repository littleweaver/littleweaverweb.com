# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20151124_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.ForeignKey(default=1, to='core.AuthorProfile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='authorprofile',
            name='twitter_username',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
