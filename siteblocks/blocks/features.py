from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class Feature(blocks.StructBlock):



    feature_item = blocks.ListBlock(

        blocks.StructBlock([
            ('title', blocks.CharBlock(default="Title", required=False)),
            ('description', blocks.TextBlock(default="RichText", required=False)),
        ])
    )

    class Meta:
        template = 'site_blocks/feature_item.html'
        icon = 'image'


