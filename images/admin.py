from django.contrib import admin
from .models import Image

# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ['title', 'slug', 'image', 'description']
    list_filter = ['created']
