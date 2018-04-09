# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Project, Story, Block

from django.contrib import admin

# Register your models here.

class BlockInline(admin.StackedInline):
    model = Block

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        BlockInline,
    ]
