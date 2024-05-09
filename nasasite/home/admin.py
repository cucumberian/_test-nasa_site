from django.contrib import admin
from django.utils.safestring import mark_safe

from adminsortable2.admin import SortableAdminMixin

from .models import SliderImage


@admin.register(SliderImage)
class ImageSliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["image", "get_icon", "order_index"]

    def get_icon(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width=50>')
        return "Нет изображения"

    get_icon.short_description = "Миниатюрка"
