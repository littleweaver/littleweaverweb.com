from django.db import models

from django.shortcuts import render, get_object_or_404
from django.utils.six import text_type
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailadmin.utils import send_mail
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.rich_text import features
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel, InlinePanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from blocks import CodeBlock, QuoteBlock, MarkdownBlock, CaptionedImageBlock


@register_setting
class OpenGraphAndMetaSettings(BaseSetting):
    open_graph_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True,
                              on_delete=models.SET_NULL)

    meta_description = models.CharField(
        max_length=255,
        help_text='meta[name="description"] and og:description')

    ga_id = models.CharField(
        null=True,
        blank=True,
        max_length=30,
        help_text='Google Analytics Tracking ID, e.g., UA-12345678-1')

    panels = [
        ImageChooserPanel('open_graph_image'),
        FieldPanel('meta_description'),
        FieldPanel('ga_id'),
    ]

    class Meta:
        verbose_name = 'Head Meta'


@register_snippet
class Service(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


@register_snippet
class Technology(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(
        max_length=255,
        blank=True,
        help_text='External URL for the technology')
    logo = models.TextField(
        blank=True,
        help_text="SVG contents. It is recommended to use a compressor such as https://jakearchibald.github.io/svgomg/ and remove width/height attributes. It should always have a viewBox attribute.")

    class Meta:
        verbose_name_plural = 'technologies'
        ordering = ('name',)

    def __unicode__(self):
        return self.name


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
        ('image', CaptionedImageBlock()),
    ])
    screenshot = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name="+")
    background_photo = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                           on_delete=models.SET_NULL,
                           help_text="Background image for homepage stripe. Should be blurred or low entropy for light text to be legible on it.",
                           related_name="+")
    client_name = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    project_date = models.DateField(blank=True, null=True,
                            help_text="Approximate date of project completion.")
    link = models.URLField(max_length=255, null=True, blank=True,
                            help_text="External URL of the project.",
                            verbose_name="Client External URL")
    services = ParentalManyToManyField(Service, blank=True)
    technologies = ParentalManyToManyField(Technology, blank=True)

    # Details for teasers on other pages:
    teaser_title = models.CharField(max_length=255, blank=True)
    teaser_description = RichTextField(blank=True)

    parent_page_types = ['core.WorkListPage']

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('link'),
            ImageChooserPanel('screenshot'),
            FieldPanel('client_name'),
            FieldPanel('project_name'),
            FieldPanel('project_date'),
            FieldPanel('services'),
            FieldPanel('technologies'),
        ], "Project Details")
    ]

    promote_panels = Page.promote_panels + [
        MultiFieldPanel([
            FieldPanel('teaser_title'),
            FieldPanel('teaser_description'),
            ImageChooserPanel('background_photo'),
        ], "Teaser Details"),
    ]

class AuthorPage(Page):
    picture = models.ForeignKey("wagtailimages.Image", blank=True, null=True,
                                on_delete=models.SET_NULL, related_name='+')
    bio = RichTextField(blank=True)
    is_member = models.BooleanField(default=False)
    name = models.CharField(max_length=200, blank=True)
    twitter_username = models.CharField(max_length=15, blank=True)
    github_username = models.CharField(max_length=30, blank=True)
    # portfolio_link = models.CharField(max_length=50, blank=True)
    # banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
    #                                  on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        ImageChooserPanel('picture'),
        FieldPanel('bio'),
        FieldPanel('is_member'),
        FieldPanel('twitter_username'),
        FieldPanel('github_username'),
        # FieldPanel('portfolio_link'),
        # ImageChooserPanel('banner_image'),
    ]

    def get_context(self, request):
        context = super(AuthorPage, self).get_context(request)
        context['blog_entries'] = BlogPage.objects.filter(author=self).live()
        return context

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
        context['members'] = AuthorPage.objects.filter(is_member=True).order_by('?')
        return context


class ServicesPage(Page):
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('code', CodeBlock(icon='code')),
        ('quote', QuoteBlock(icon='openquote')),
        ('markdown', MarkdownBlock()),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', CaptionedImageBlock()),
    ])
    banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                                     on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        ImageChooserPanel('banner_image'),
        InlinePanel('services', label="Services"),
        InlinePanel('technologies', label="Technologies"),
    ]

    def get_context(self, request):
        context = super(ServicesPage, self).get_context(request)
        context['technologies'] = Technology.objects.filter(technologysection__page=self)
        return context


class ServiceSection(Orderable):
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


class TechnologySection(Orderable):
    page = ParentalKey(ServicesPage, related_name='technologies')
    technology = models.ForeignKey(Technology)

    panels = [
        SnippetChooserPanel('technology'),
    ]


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('core.BlogPage', related_name='tagged_items')

class BlogPage(Page):
    author = models.ForeignKey('core.AuthorPage', null=True, blank=True,
                               on_delete=models.SET_NULL,)
    publication_date = models.DateField(
        help_text="Past or future date of publication")
    summary = models.TextField(help_text="Intro or short summary of post")
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(
            icon='doc-full',
            label='Rich Text',
            features=[
                # Default features
                'h2',
                'h3',
                'h4',
                'hr',
                'link',
                'bold',
                'italic',
                'ol',
                'ul',
                'document-link',
                'embed',
                'image',

                # Extra features
                'code',
            ],
        )),
        ('code', CodeBlock(icon='code')),
        ('quote', QuoteBlock(icon='openquote')),
        ('markdown', MarkdownBlock()),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', CaptionedImageBlock()),
    ])
    banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                                     on_delete=models.SET_NULL)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    teaser_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True,
                           on_delete=models.SET_NULL,
                           help_text="Image to display on the blog index page",
                           related_name="+")

    content_panels = Page.content_panels + [
        PageChooserPanel('author'),
        FieldPanel('publication_date'),
        FieldPanel('summary'),
        StreamFieldPanel('body'),
        ImageChooserPanel('banner_image'),
    ]
    parent_page_types = ['BlogIndexPage']
    promote_panels = Page.promote_panels + [
        MultiFieldPanel([
            ImageChooserPanel('teaser_image'),
        ], "Teaser Details"),
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

    def process_form_submission(self, form):
        super(AbstractEmailForm, self).process_form_submission(form)

        if self.to_address:
            content = '\n'.join([x[1].label + ': ' + text_type(form.data.get(x[0])) for x in form.fields.items()])
            if 'your-name' in form.data and 'your-email' in form.data:
                subject = u'{}: {} <{}>'.format(self.subject, form.data['your-name'], form.data['your-email'])
            else:
                subject = self.subject
            send_mail(subject, content, [self.to_address], self.from_address,)
