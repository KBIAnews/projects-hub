# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Project, Story, Block

from django.contrib import admin

# Register your models here.

class BlockInline(admin.StackedInline):
    model = Block
    readonly_fields = ["id"]
    fieldsets = (
        (None, {
            'fields': (
                ('order','id',),
            )
        }),
        ('Text and HTML Options', {
            'classes': ('collapse',),
            'fields': (
                'text',
            )
        }),)

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
    fieldsets = (
        (None, {
            'fields': (
                ('name', 'slug'),
                ('project', 'order'),
                'teaser',
                'text',
            ),
        }),
        ('Media', {
            'fields':  (
                'teaser_image',
                'audio',
            )
        }),
    )
