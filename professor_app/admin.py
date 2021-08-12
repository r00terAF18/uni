from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from .models import *


class PUploadInline(StackedInline):
    model = ProfessorUpload
    extra = 1
    show_change_link = True


class PPostInline(StackedInline):
    model = ProfessorPost
    extra = 1
    show_change_link = True



@admin.register(Professor)
class PAdmin(ModelAdmin):
    inlines = [PUploadInline, PPostInline]
    # pass

