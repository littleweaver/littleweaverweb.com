# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import core.models
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_blogindexpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('twitter_username', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'rich_text', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Rich Text', icon=b'doc-full')), (b'code', core.models.CodeBlock(icon=b'code')), (b'quote', core.models.QuoteBlock(icon=b'openquote')), (b'html', wagtail.wagtailcore.blocks.RawHTMLBlock(label=b'HTML', icon=b'site')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock())]),
        ),
    ]
