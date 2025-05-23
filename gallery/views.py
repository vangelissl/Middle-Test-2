from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from datetime import timedelta
from .models import Image, Category


def gallery_view(request):
    month_ago = now() - timedelta(days=30)
    images = Image.objects.filter(
        created_date__gte=month_ago
    )

    return render(request, 'gallery.html', {
        'images': images})


def image_detail(request, pk):
    image = get_object_or_404(Image, pk=id)

    return render(request, 'image_detail.html', {
        'image': image})
