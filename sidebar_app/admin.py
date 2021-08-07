from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from .models import *


class SideBarItemInline(TabularInline):
    model = SidebarItem
    prepopulated_fields = {"sidebar_link": ("sidebar_item_title",)}
    extra = 1
    show_change_link = True


@admin.register(Sidebar)
class SideBarAdmin(ModelAdmin):
    inlines = [SideBarItemInline]
