from django.utils.safestring import mark_safe

from markdown import markdown
from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class CodeBlock(blocks.StructBlock):
    """
    Code Highlighting Block
    """
    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('js', 'Javascript'),
        ('bash', 'Bash/Shell'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('scss', 'SCSS'),
        ('php', 'PHP'),
    )

    language = blocks.ChoiceBlock(choices=LANGUAGE_CHOICES)
    code = blocks.TextBlock()

    class Meta:
        icon = 'code'

    def render(self, value):
        src = value['code'].strip('\n')
        lang = value['language']

        lexer = get_lexer_by_name(lang)
        formatter = get_formatter_by_name(
            'html',
            linenos=None,
            cssclass='codehilite',
            style='default',
            noclasses=False,
        )
        return mark_safe(highlight(src, lexer, formatter))


class QuoteBlock(blocks.StructBlock):

    quote = blocks.RichTextBlock()
    credit = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'core/blocks/quote.html'
        icon = 'openquote'
        label = 'Quote'


class MarkdownBlock(blocks.TextBlock):
    class Meta:
        icon = 'code'

    def render_basic(self, value):
        md = markdown(
            value,
            [
                'markdown.extensions.fenced_code',
                'codehilite',
            ],
        )
        return mark_safe(md)


class CaptionedImageBlock(blocks.StructBlock):

    image = ImageChooserBlock()
    caption = blocks.RichTextBlock(required=False)
    is_screenshot = blocks.BooleanBlock(required=False,
                        help_text="Display image in a mock broswer window. Must be 810px wide, or 1110px wide if displayed full-width.")
    full_width = blocks.BooleanBlock(required=False,
                        help_text="Display image at the full width of the container. IF also a screenshot, must be at least 1110px wide.")

    class Meta:
        template = 'core/blocks/captioned_image.html'
        icon = 'image'
        label = 'Captioned Image'
