from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.images.blocks import ImageChooserBlock


class Partners(blocks.StructBlock):



    partner = blocks.ListBlock(

        blocks.StructBlock([

            ('image', ImageChooserBlock(required=False)),

        ])
    )

    class Meta:
        template = 'site_blocks/partner.html'
        icon = 'image'


