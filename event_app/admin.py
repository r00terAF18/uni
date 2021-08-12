from django.contrib import admin

from .models import Event


# custom action for multi selecting
def this_publish(modeladmin, request, queryset):
    queryset.update(draft=True)


this_publish.short_description = "فعال کردن انتخاب شده"


def this_draft(modeladmin, request, queryset):
    queryset.update(draft=False)


this_draft.short_description = "غیر فعال سازی انتخواب شده"


@admin.register(Event)
class EventAdminModel(admin.ModelAdmin):
    actions = [this_publish, this_draft]
    list_display = ["event_date", "title", "draft"]
    list_editable = ["draft"]


