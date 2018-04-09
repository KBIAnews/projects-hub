# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Primary Key generator algorithm.
def pkgen():
    from base64 import b32encode
    from hashlib import sha1
    from random import random
    rude = ('moose',)
    bad_pk = True
    while bad_pk:
        pk = b32encode(sha1(str(random())).digest()).lower()[:10]
        bad_pk = False
        for rw in rude:
            if pk.find(rw) >= 0: bad_pk = True
    return pk

# Create your models here

class Project (models.Model):
    slug = models.SlugField(max_length=128,
                            unique=True,
                            blank=False,
                            null=False)

    name = models.CharField(max_length=512,
                            blank=False,
                            null=False)
    def __str__(self):
        return "%s" % self.name

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
    teaser_image = models.ImageField("Image that appears on project page in designs.",
                                     null=True,
                                     blank=True)
    audio = models.FileField(help_text="Story audio - upload as MP3.",
                             null=True,
                             blank=True)

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return "/%s/%s/" % (self.project.slug, self.slug)

    class Meta:
        ordering = ['order','slug']

class Block (models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=pkgen)
    story = models.ForeignKey(Story,
                              null=False,
                              blank=False)
    text = models.TextField(help_text="Block interpreted text - used only in HTML and Markdown blocks.",
                            null=True,
                            blank=True)

    def __str__(self):
        return "%s in %s" % (self.id, self.story.name)
