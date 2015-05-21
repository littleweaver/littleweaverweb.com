from django.db import models

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


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
    subpage_types = ['core.WorkPage',]

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

    parent_page_types = ['core.WorkListPage',]

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
