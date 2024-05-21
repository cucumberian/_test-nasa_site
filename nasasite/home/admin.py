from django.contrib import admin
from django.utils.safestring import mark_safe

from adminsortable2.admin import SortableAdminMixin
from easy_thumbnails.files import get_thumbnailer

from .models import SliderImage


@admin.register(SliderImage)
class ImageSliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["image", "get_icon", "order_index"]

    def get_icon(self, object):
        if object.image:
            thumbnailer = get_thumbnailer(object.image)
            thumbnailer_options = {
                "size": (50, 50),
                "crop": True,
            }
            thumb_url = thumbnailer.get_thumbnail(thumbnailer_options).url
            return mark_safe("<img src='"+ thumb_url + "' >")
        return "Нет изображения"

    get_icon.short_description = "Миниатюрка"
