from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.images.blocks import ImageChooserBlock


class Foods(blocks.StructBlock):



    food_item = blocks.ListBlock(

        blocks.StructBlock([
            ('title', blocks.CharBlock(default="Title", required=False)),
            ('price', blocks.TextBlock(default="price", required=False)),
            ('image', ImageChooserBlock(required=False)
),

        ])
    )

    class Meta:
        template = 'site_blocks/foods.html'
        icon = 'image'


