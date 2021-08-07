from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from .models import *

# custom action for multi selecting
def this_publish(modeladmin, request, queryset):
    queryset.update(draft=True)


this_publish.short_description = "فعال کردن انتخاب شده"


def this_draft(modeladmin, request, queryset):
    queryset.update(draft=False)


this_draft.short_description = "غیر فعال سازی انتخواب شده"

# Defining Tabular Inlines
class PageContentInline(TabularInline):
    model = SubMenuPage
    extra = 1
    show_change_link = True


@admin.register(SubMenu)
class MenuAdmin(ModelAdmin):
    inlines = [PageContentInline]


admin.site.register(Menu)
