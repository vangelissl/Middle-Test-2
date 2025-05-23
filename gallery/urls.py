from django.urls import path
from .views import gallery_view, image_detail

urlpatterns = [
    path('', gallery_view, name='gallery'),
    path('images/<int:id>/', image_detail, name='image_detail'),
]