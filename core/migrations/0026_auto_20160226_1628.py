# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def testimonial_to_stream_quote(apps, schema_editor):
    WorkPage = apps.get_model("core", "WorkPage")
    db_alias = schema_editor.connection.alias
    for page in WorkPage.objects.using(db_alias).all():
        if page.testimonial:
            page.body.stream_data.insert(0,
                {'type': 'quote',
                 'value': {'credit': page.testimonial_credit,
                           'quote': page.testimonial}})
            page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20160218_0102'),
    ]

    operations = [
        migrations.RunPython(
            testimonial_to_stream_quote
        ),

        migrations.RemoveField(
            model_name='workpage',
            name='testimonial',
        ),
        migrations.RemoveField(
            model_name='workpage',
            name='testimonial_credit',
        ),
    ]
