from django.shortcuts import render

from .models import SliderImage


def index(request):
    slider_images = SliderImage.objects.all().order_by("order_index")
    context = {
        "slider_images": slider_images,
    }
    return render(
        request=request,
        template_name="home/index.html",
        context=context,
    )
