# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Project (models.Model):
    slug = models.SlugField(max_length=128,
                            unique=True,
                            blank=False,
                            null=False)

    name = models.CharField(max_length=512,
                            blank=False,
                            null=False)

    def get_absolute_url(self):
        return "/%s/" % self.slug

    class Meta:
        ordering = ['slug']

class Story (models.Model):
    slug = models.SlugField(max_length=128,
                            unique=True,
                            blank=False,
                            null=False)

    name = models.CharField(max_length=512,
                            blank=False,
                            null=False)
    teaser = models.TextField(max_length=1024,
                            blank=False,
                            null=False)
    project = models.ForeignKey(Project,
                                null=False,
                                blank=False)
    order = models.IntegerField(null=False,
                                blank=False)
    text = models.TextField(help_text="Story text - in Markdown. Appears before block structure.")


    def get_absolute_url(self):
        return "/%s/" % self.project.slug

    class Meta:
        ordering = ['order','slug']
