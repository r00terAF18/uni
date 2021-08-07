from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from .models import *


class CarouselItemInline(TabularInline):
    model = CarouselItem
    extra = 1
    show_change_link = False


@admin.register(Carousel)
class CarouselAdmin(ModelAdmin):
    inlines = [CarouselItemInline]
    list_display = ["is_active"]
