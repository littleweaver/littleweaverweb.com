from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class SimplePage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class HomePage(Page):
    featured_work = models.ForeignKey('WorkPage', null=True, blank=True,
                                      on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        PageChooserPanel('featured_work'),
    ]


class WorkListPage(Page):
    body = RichTextField()
    subpage_types = ['core.WorkPage']

    content_panels = Page.content_panels  + [FieldPanel('body', classname="full")]


class WorkPage(Page):

    body = RichTextField()
    screenshot = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name="+")
    client_name = models.CharField(max_length=255)
    project_date = models.DateField(blank=True, null=True,
                            help_text="Approximate date of project completion.")

    # Details for teasers on other pages:
    teaser_title = models.CharField(max_length=255, blank=True)
    teaser_description = RichTextField(blank=True)

    parent_page_types = ['core.WorkListPage']

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        MultiFieldPanel([
            ImageChooserPanel('screenshot'),
            FieldPanel('client_name'),
            FieldPanel('project_date'),
        ], "Project Details")
    ]

    promote_panels = Page.promote_panels + [
        MultiFieldPanel([
            FieldPanel('teaser_title'),
            FieldPanel('teaser_description')
        ], "Teaser Details"),
    ]


class AboutPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class CodeBlock(blocks.TextBlock):
    class Meta:
        template = 'core/blocks/code.html'
        icon = 'code'
        label = 'Code'


class QuoteBlock(blocks.TextBlock):
    class Meta:
        template = 'core/blocks/quote.html'
        icon = 'openquote'
        label = 'Quote'


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('core.BlogPage', related_name='tagged_items')


class BlogPage(Page):
    author = models.ForeignKey('core.AuthorProfile', null=True, blank=True,
                               on_delete=models.SET_NULL,)
    publication_date = models.DateField(
        help_text="Past or future date of publication")
    summary = models.TextField(help_text="Intro or short summary of post")
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('code', CodeBlock(icon='code')),
        ('quote', QuoteBlock(icon='openquote')),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', ImageChooserBlock()),
    ])
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        SnippetChooserPanel('author'),
        FieldPanel('publication_date'),
        FieldPanel('summary'),
        StreamFieldPanel('body'),
    ]
    parent_page_types = ['BlogIndexPage']
    promote_panels = [
        FieldPanel('tags'),
    ]

    def get_context(self, request):
        context = super(BlogPage, self).get_context(request)
        context['blog_index'] = BlogIndexPage.objects.first()
        return context


class BlogIndexPage(Page):
    intro = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('intro'),
    ]
    subpage_types = ['BlogPage']

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)

        # Add extra variables and return the updated context
        context['blog_entries'] = BlogPage.objects.child_of(self).live()
        return context


@register_snippet
class AuthorProfile(models.Model):
    name = models.CharField(max_length=100)
    twitter_username = models.CharField(max_length=15, null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('twitter_username'),
    ]

    def __str__(self):              # __unicode__ on Python 2
        return self.name
