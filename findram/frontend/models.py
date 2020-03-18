from django.utils import timezone
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

all_features = [  # 'h1', 'h2', 'h3',
    'h4',  # 'h5', 'h6',
    'bold', 'italic', 'underline', 'ol', 'ul', 'hr',
    'link',
    'document-link', 'image', 'embed',
    'code',  # 'superscript', 'subscript', 'strikethrough',
    'blockquote']


class PortfolioItemTag(TaggedItemBase):
    content_object = ParentalKey('frontend.PortfolioItem')


class PortfolioItem(ClusterableModel, Orderable):
    """Repeated subpanel steps"""
    page = ParentalKey('frontend.HomePage', related_name="portfolio_items")
    item_title = models.CharField(null=True, blank=True, max_length=200)
    item_tags = ClusterTaggableManager(through=PortfolioItemTag, blank=True)
    item_description = RichTextField(blank=True, features=all_features)
    item_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="+")
    item_link = models.URLField(max_length=200, blank=True)
    item_sourcecode_link = models.URLField(max_length=200, blank=True)
    item_blogpost_link = models.URLField(max_length=200, blank=True)
    in_progress = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    panels = [
        FieldPanel('item_title'),
        FieldPanel('item_tags'),
        FieldPanel('item_description'),
        ImageChooserPanel('item_image'),
        FieldPanel('item_link'),
        FieldPanel('item_sourcecode_link'),
        FieldPanel('item_blogpost_link'),
        FieldPanel('in_progress'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),

    ]


class HomePage(Page):
    max_count = 1
    template = "frontend/home_page.html"

    banner_title = RichTextField(blank=True, features=all_features)
    banner_blurb = RichTextField(blank=True, features=all_features)
    aboutme_text = RichTextField(blank=True, features=all_features)
    aboutme_photo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=False, related_name='+'
    )

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            FieldPanel('banner_title', classname="full"),
            FieldPanel('banner_blurb', classname="full"),
        ], heading="Banner"),

        MultiFieldPanel([
            FieldPanel('aboutme_text', classname="full"),
            ImageChooserPanel('aboutme_photo'),
        ], heading="About me"),

        MultiFieldPanel([
            InlinePanel('portfolio_items', min_num=1, label='portfolio item'),
        ], heading="Portfolio items"),
    ]


class BlogPage(Page):
    max_count = 1
    template = "frontend/blog_page.html"

    banner_title = RichTextField(blank=True, features=all_features)
    banner_blurb = RichTextField(blank=True, features=all_features)

    content_panels = Page.content_panels + [
        FieldPanel('banner_title', classname="full"),
        FieldPanel('banner_blurb', classname="full")
    ]


class BlogPostTag(TaggedItemBase):
    content_object = ParentalKey('frontend.PostPage')


class PostPage(Page):
    template = "frontend/post_page.html"

    body = RichTextField(blank=True, features=all_features)
    blurb = RichTextField(blank=True, features=all_features)
    seo_description = models.CharField(blank=True, null=True, max_length=150)
    author = models.CharField(default="Ram Parameswaran", blank=True, null=True, max_length=200)
    tags = ClusterTaggableManager(through=BlogPostTag, blank=True)
    cover_photo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=False, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('blurb', classname="full"),
        FieldPanel('seo_description', classname="full"),
        FieldPanel('author', classname="full"),
        FieldPanel('tags', classname="full"),
        ImageChooserPanel('cover_photo'),
    ]
