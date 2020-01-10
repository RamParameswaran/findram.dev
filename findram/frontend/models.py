from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from modelcluster.models import ClusterableModel
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


class PortfolioItemTag(TaggedItemBase):
    content_object = ParentalKey('frontend.PortfolioItem')


class PortfolioItem(ClusterableModel, Orderable):
    """Repeated subpanel steps"""
    page = ParentalKey('frontend.HomePage', related_name="portfolio_items")
    item_title = models.CharField(null=True, blank=True, max_length=200)
    item_tags = ClusterTaggableManager(through=PortfolioItemTag, blank=True)
    item_description = RichTextField(blank=True)
    item_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="+")
    item_link = models.URLField(max_length=200, blank=True)
    item_sourcecode_link = models.URLField(max_length=200, blank=True)
    item_blogpost_link = models.URLField(max_length=200, blank=True)

    panels = [
        FieldPanel('item_title'),
        FieldPanel('item_tags'),
        FieldPanel('item_description'),
        ImageChooserPanel('item_image'),
        FieldPanel('item_link'),
        FieldPanel('item_sourcecode_link'),
        FieldPanel('item_blogpost_link'),
    ]


class HomePage(Page):
    banner_title = RichTextField(blank=True)
    banner_blurb = RichTextField(blank=True)
    banner_avatar = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=False, related_name='+'
    )

    aboutme_text = RichTextField(blank=True)
    aboutme_photo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=False, related_name='+'
    )

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            FieldPanel('banner_title', classname="full"),
            FieldPanel('banner_blurb', classname="full"),
            ImageChooserPanel('banner_avatar'),
        ], heading="Banner"),

        MultiFieldPanel([
            FieldPanel('aboutme_text', classname="full"),
            ImageChooserPanel('aboutme_photo'),
        ], heading="About me"),

        MultiFieldPanel([
            InlinePanel('portfolio_items', min_num=1, label='portfolio item'),
        ], heading="Portfolio items"),





    ]
