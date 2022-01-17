from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroImage(blocks.StructBlock):
    title = blocks.CharBlock(default="Title", required=False)
    background_image = ImageChooserBlock(help_text="Entre your image")

    class Meta:
        template = 'site_blocks/hero_image.html'
        icon = 'image'
