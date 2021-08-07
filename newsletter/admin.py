from django.contrib import admin

from .models import *

# custom action for multi selecting
def this_send(modeladmin, request, queryset):
    for q in queryset:
        q = NewsletterMessage.objects.get(pk=q.pk)
        q.send_message()


this_send.short_description = "Send Message to subscribers"


@admin.register(NewsletterMessage)
class NMAdmin(admin.ModelAdmin):
    actions = [this_send]


admin.site.register(Subscriber)
