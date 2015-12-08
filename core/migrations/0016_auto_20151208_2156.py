# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import core.blocks
import wagtail.wagtailimages.blocks
import django.db.models.deletion
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('core', '0015_auto_20151201_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorprofile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='authorprofile',
            name='github_username',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='authorprofile',
            name='is_member',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='authorprofile',
            name='picture',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='authorprofile',
            name='twitter_username',
            field=models.CharField(default='', max_length=15, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'rich_text', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Rich Text', icon=b'doc-full')), (b'code', wagtail.wagtailcore.blocks.StructBlock([(b'language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'python', b'Python'), (b'js', b'Javascript'), (b'bash', b'Bash/Shell'), (b'html', b'HTML'), (b'css', b'CSS'), (b'scss', b'SCSS'), (b'php', b'PHP')])), (b'code', wagtail.wagtailcore.blocks.TextBlock())], icon=b'code')), (b'quote', core.blocks.QuoteBlock(icon=b'openquote')), (b'markdown', core.blocks.MarkdownBlock()), (b'html', wagtail.wagtailcore.blocks.RawHTMLBlock(label=b'HTML', icon=b'site')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock())]),
        ),
    ]
