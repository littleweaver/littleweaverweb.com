# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('core', '0029_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenGraphAndMetaSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('open_graph_image_path', models.CharField(help_text=b'Absolute path to og:image, e.g. /static/images/facebook.gif', max_length=255)),
                ('meta_description', models.CharField(help_text=b'meta[name="description"] and og:description', max_length=200)),
                ('site', models.OneToOneField(editable=False, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
