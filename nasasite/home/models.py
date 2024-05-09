from django.db import models

from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    image = FilerImageField(
        null=False,
        blank=False,
        verbose_name="изображение слайдера",
        on_delete=models.CASCADE,
    )
    order_index = models.PositiveIntegerField(
        default=0, blank=False, null=False, verbose_name="Сортировка"
    )
    alt_text = models.TextField(
        default="",
        blank=True,
        null=True,
        verbose_name="Альтернативный текст",
    )

    @property
    def filename(self):
        return self.image.original_filename

    class Meta:
        verbose_name = "Картинка слайдера"
        verbose_name_plural = "Картинки слайдера"
        ordering = ["order_index"]
