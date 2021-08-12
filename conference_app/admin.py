from django.contrib import admin

from .models import Conference


# custom action for multi selecting
def this_publish(modeladmin, request, queryset):
    queryset.update(draft=True)


this_publish.short_description = "فعال کردن انتخاب شده"


def this_draft(modeladmin, request, queryset):
    queryset.update(draft=False)


this_draft.short_description = "غیر فعال سازی انتخواب شده"

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    actions = [this_publish, this_draft]
    list_display = ["title", "date_created", "draft"]
    list_editable = ["draft"]

    def save_model(self, request, obj, form, change) -> None:
        obj.written_by = request.user
        return super().save_model(request, obj, form, change)


