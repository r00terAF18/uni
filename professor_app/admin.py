from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from .models import *


class PUploadInline(TabularInline):
    model = ProfessorUpload
    extra = 1
    show_change_link = True


class PPostInline(TabularInline):
    model = ProfessorPost
    extra = 1
    show_change_link = True


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


@admin.register(Professor)
class PAdmin(ModelAdmin):
    inlines = [PUploadInline, PPostInline]
