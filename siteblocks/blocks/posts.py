from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.images.blocks import ImageChooserBlock


class Posts(blocks.StructBlock):



    post = blocks.ListBlock(

        blocks.StructBlock([
            ('title', blocks.CharBlock(default="Title", required=False)),
            ('body', blocks.TextBlock(default="RichText", required=False)),
            ('image', ImageChooserBlock(required=False)
),

        ])
    )

    class Meta:
        template = 'site_blocks/post.html'
        icon = 'image'


