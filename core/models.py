from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel, InlinePanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from blocks import CodeBlock, QuoteBlock, MarkdownBlock


class SimplePage(Page):
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('code', CodeBlock(icon='code')),
        ('quote', QuoteBlock(icon='openquote')),
        ('markdown', MarkdownBlock()),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', ImageChooserBlock()),
    ])
    banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                                     on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        ImageChooserPanel('banner_image'),
        StreamFieldPanel('body'),
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

    content_panels = Page.content_panels + [FieldPanel('body', classname="full")]


class WorkPage(Page):
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('code', CodeBlock(icon='code')),
        ('quote', QuoteBlock(icon='openquote')),
        ('markdown', MarkdownBlock()),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', ImageChooserBlock()),
    ])
    screenshot = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name="+")
    background_photo = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                           on_delete=models.SET_NULL,
                           help_text="Background image for homepage stripe. Should be blurred or low entropy for light text to be legible on it.",
                           related_name="+")
    client_name = models.CharField(max_length=255)
    client_external_url = models.CharField(max_length=255, null=True, blank=True,
                            help_text="External URL of the project.",
                            verbose_name="Client External URL")
    project_date = models.DateField(blank=True, null=True,
                            help_text="Approximate date of project completion.")
    testimonial = RichTextField(blank=True)
    testimonial_credit = models.CharField(max_length=255, blank=True)

    # Details for teasers on other pages:
    teaser_title = models.CharField(max_length=255, blank=True)
    teaser_description = RichTextField(blank=True)

    parent_page_types = ['core.WorkListPage']

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('testimonial'),
            FieldPanel('testimonial_credit'),
        ], "Testimonial"),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            ImageChooserPanel('screenshot'),
            FieldPanel('client_name'),
            FieldPanel('client_external_url'),
            FieldPanel('project_date'),
        ], "Project Details")
    ]

    promote_panels = Page.promote_panels + [
        MultiFieldPanel([
            FieldPanel('teaser_title'),
            FieldPanel('teaser_description'),
            ImageChooserPanel('background_photo'),
        ], "Teaser Details"),
    ]


class AboutPage(Page):
    body = RichTextField()
    banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                                     on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('banner_image'),
    ]

    def get_context(self, request):
        context = super(AboutPage, self).get_context(request)
        context['members'] = AuthorProfile.objects.filter(is_member=True).order_by('?')
        return context


class ServicesPage(Page):
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('code', CodeBlock(icon='code')),
        ('quote', QuoteBlock(icon='openquote')),
        ('markdown', MarkdownBlock()),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', ImageChooserBlock()),
    ])
    banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                                     on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        ImageChooserPanel('banner_image'),
        InlinePanel('services', label="Services")
    ]


class Service(Orderable):
    page = ParentalKey(ServicesPage, related_name='services')
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True,
                              on_delete=models.SET_NULL)
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('body')
    ]


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
        ('markdown', MarkdownBlock()),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', ImageChooserBlock()),
    ])
    banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                                     on_delete=models.SET_NULL)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        SnippetChooserPanel('author'),
        FieldPanel('publication_date'),
        FieldPanel('summary'),
        StreamFieldPanel('body'),
        ImageChooserPanel('banner_image'),
    ]
    parent_page_types = ['BlogIndexPage']
    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]

    def get_context(self, request):
        context = super(BlogPage, self).get_context(request)
        context['blog_index'] = BlogIndexPage.objects.first()
        return context


class BlogIndexPage(Page):
    banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                                     on_delete=models.SET_NULL)
    intro = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        ImageChooserPanel('banner_image'),
        StreamFieldPanel('intro'),
    ]
    subpage_types = ['BlogPage']

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)

        entries = BlogPage.objects.child_of(self).live().order_by('-publication_date')
        tag = request.GET.get('tag')
        if tag:
            entries = entries.filter(tags__name=tag)

        # Add extra variables and return the updated context
        context['blog_entries'] = entries
        return context


@register_snippet
class AuthorProfile(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ForeignKey("wagtailimages.Image", blank=True, null=True,
                                on_delete=models.SET_NULL, related_name='+')
    bio = RichTextField(blank=True)
    is_member = models.BooleanField(default=False)
    twitter_username = models.CharField(max_length=15, blank=True)
    github_username = models.CharField(max_length=30, blank=True)

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('picture'),
        FieldPanel('bio'),
        FieldPanel('is_member'),
        FieldPanel('twitter_username'),
        FieldPanel('github_username'),
    ]

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class EmailFormField(AbstractFormField):
    page = ParentalKey('EmailFormPage', related_name='form_fields')


class EmailFormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                                     on_delete=models.SET_NULL)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('banner_image'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldPanel('to_address', classname="full"),
            FieldPanel('from_address', classname="full"),
            FieldPanel('subject', classname="full"),
        ], "Email")
    ]
