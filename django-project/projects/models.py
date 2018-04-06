# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Project (models.Model):
    slug = models.SlugField(max_length=128,
                            unique=True,
                            blank=False,
                            null=False)

    name = models.TextField(max_length=512,
                            blank=False,
                            null=False)

    def get_absolute_url(self):
        return "/%s/" % self.slug

    class Meta:
        ordering = ['slug']