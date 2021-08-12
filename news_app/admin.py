from django.contrib import admin
from django.contrib.sites.models import Site

from .models import *


# custom action for multi selecting
def this_publish(modeladmin, request, queryset):
    queryset.update(draft=True)


this_publish.short_description = "فعال کردن انتخاب شده"


def this_draft(modeladmin, request, queryset):
    queryset.update(draft=False)


this_draft.short_description = "غیر فعال سازی انتخواب شده"

# Inline models for better viewing subsets
class NewsInline(admin.StackedInline):
    model = NewsPost
    extra = 1
    show_change_link = True


# Model registiriation


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    actions = [this_publish, this_draft]
    list_display = ["title", "date_created", "draft", "target_dep"]
    list_filter = (
        "date_created",
        "draft",
    )
    search_fields = ("title",)
    list_editable = ["draft"]
    date_hierarchy = "date_created"
    list_per_page = 5
    view_on_site = False

    def save_model(self, request, obj, form, change) -> None:
        obj.written_by = request.user
        return super().save_model(request, obj, form, change)




# strange thing to do, but
admin.site.unregister(Site)
