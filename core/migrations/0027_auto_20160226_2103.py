# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import core.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20160226_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'rich_text', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Rich Text', icon=b'doc-full')), (b'code', wagtail.wagtailcore.blocks.StructBlock([(b'language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'python', b'Python'), (b'js', b'Javascript'), (b'bash', b'Bash/Shell'), (b'html', b'HTML'), (b'css', b'CSS'), (b'scss', b'SCSS'), (b'php', b'PHP')])), (b'code', wagtail.wagtailcore.blocks.TextBlock())], icon=b'code')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.RichTextBlock()), (b'credit', wagtail.wagtailcore.blocks.RichTextBlock())], icon=b'openquote')), (b'markdown', core.blocks.MarkdownBlock()), (b'html', wagtail.wagtailcore.blocks.RawHTMLBlock(label=b'HTML', icon=b'site')), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock()), (b'is_screenshot', wagtail.wagtailcore.blocks.BooleanBlock())]))]),
        ),
    ]
