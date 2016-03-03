# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20160302_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'rich_text', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Rich Text', icon=b'doc-full')), (b'code', wagtail.wagtailcore.blocks.StructBlock([(b'language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'python', b'Python'), (b'js', b'Javascript'), (b'bash', b'Bash/Shell'), (b'html', b'HTML'), (b'css', b'CSS'), (b'scss', b'SCSS'), (b'php', b'PHP')])), (b'code', wagtail.wagtailcore.blocks.TextBlock())], icon=b'code')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.RichTextBlock()), (b'credit', wagtail.wagtailcore.blocks.RichTextBlock(required=False))], icon=b'openquote')), (b'markdown', core.blocks.MarkdownBlock()), (b'html', wagtail.wagtailcore.blocks.RawHTMLBlock(label=b'HTML', icon=b'site')), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'is_screenshot', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display image in a mock broswer window. Must be 810px wide, or 1110px wide if displayed full-width.', required=False)), (b'full_width', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display image at the full width of the container. IF also a screenshot, must be at least 1110px wide.', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'rich_text', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Rich Text', icon=b'doc-full')), (b'code', wagtail.wagtailcore.blocks.StructBlock([(b'language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'python', b'Python'), (b'js', b'Javascript'), (b'bash', b'Bash/Shell'), (b'html', b'HTML'), (b'css', b'CSS'), (b'scss', b'SCSS'), (b'php', b'PHP')])), (b'code', wagtail.wagtailcore.blocks.TextBlock())], icon=b'code')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.RichTextBlock()), (b'credit', wagtail.wagtailcore.blocks.RichTextBlock(required=False))], icon=b'openquote')), (b'markdown', core.blocks.MarkdownBlock()), (b'html', wagtail.wagtailcore.blocks.RawHTMLBlock(label=b'HTML', icon=b'site')), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'is_screenshot', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display image in a mock broswer window. Must be 810px wide, or 1110px wide if displayed full-width.', required=False)), (b'full_width', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display image at the full width of the container. IF also a screenshot, must be at least 1110px wide.', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='workpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'rich_text', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Rich Text', icon=b'doc-full')), (b'code', wagtail.wagtailcore.blocks.StructBlock([(b'language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'python', b'Python'), (b'js', b'Javascript'), (b'bash', b'Bash/Shell'), (b'html', b'HTML'), (b'css', b'CSS'), (b'scss', b'SCSS'), (b'php', b'PHP')])), (b'code', wagtail.wagtailcore.blocks.TextBlock())], icon=b'code')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.RichTextBlock()), (b'credit', wagtail.wagtailcore.blocks.RichTextBlock(required=False))], icon=b'openquote')), (b'markdown', core.blocks.MarkdownBlock()), (b'html', wagtail.wagtailcore.blocks.RawHTMLBlock(label=b'HTML', icon=b'site')), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'is_screenshot', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display image in a mock broswer window. Must be 810px wide, or 1110px wide if displayed full-width.', required=False)), (b'full_width', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display image at the full width of the container. IF also a screenshot, must be at least 1110px wide.', required=False))]))]),
        ),
    ]
