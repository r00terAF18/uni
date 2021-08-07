from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from .models import *


class DepFormsInline(TabularInline):
    model = DepForms
    extra = 1
    show_change_link = True


class DepLabsInline(TabularInline):
    model = DepLab
    extra = 1
    show_change_link = True


@admin.register(Departmant)
class DeprtmentAdminModel(ModelAdmin):
    inlines = [DepFormsInline, DepLabsInline]
    list_display = ["name", "head"]


admin.site.register(Professor)
admin.site.register(ProfessorPost)
admin.site.register(ProfessorUpload)
