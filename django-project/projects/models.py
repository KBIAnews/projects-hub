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
                                blank=False,
                                related_name="stories")
    order = models.IntegerField(null=False,
                                blank=False)
    text = models.TextField(help_text="Story text - in Markdown. Appears before block structure.",
                            blank=True)
    teaser_image = models.ImageField(help_text="Image that appears on project page in designs.",
                                     null=True,
                                     blank=True)
    audio = models.FileField(help_text="Story audio - upload as MP3.",
                             null=True,
                             blank=True)
    author = models.CharField(max_length=280,
                              blank=True)

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return "/%s/%s/" % (self.project.slug, self.slug)

    class Meta:
        ordering = ['order','slug']
        verbose_name_plural = "stories"

class Block (models.Model):
    id = models.CharField(max_length=10,
                          primary_key=True,
                          default=pkgen,
                          verbose_name="Internal CMS ID",
                          editable=False)
    story = models.ForeignKey(Story,
                              null=False,
                              blank=False,
                              related_name="blocks")
    text = models.TextField(help_text="Block interpreted text - used only in HTML and Markdown blocks.",
                            null=True,
                            blank=True)
    order = models.IntegerField(help_text="Priority of display on story page - lowest first.")
    image_caption = models.TextField("Image Caption",
                                     null=True,
                                     blank=True)
    image_alt = models.CharField("Image 'Alt Text'",
                                 max_length=1024,
                                 null=True,
                                 blank=True,
                                 help_text="Alternate image text for screen readers and SEO. If you do not specify, this falls back to image caption.")
    image_file = models.ImageField("Image Upload",
                                   null=True,
                                   blank=True)
    image_credit = models.CharField("Image Credit",
                                    max_length=280,
                                    null=True,
                                    blank=True)
    audio_file = models.FileField("Audio MP3 Upload",
                                  null=True,
                                  blank=True)


    # Block Typing - This is where the magic happens
    # Block type choices are based closely on MIME type standard formatting.
    BLOCK_TYPE_CHOICES = (
        ('text/md', 'Markdown Formatted Text'),
        ('text/html', 'HTML Formatted Text'),
        ('text/plain|h2', 'Large Heading'),
        ('text/plain|h3', 'Small Heading'),
        ('text/plain|blockquote','Pull Quote'),
        ('image/*|full', 'Full Width Image'),
        ('image/*|contain', 'Text Width Image'),
        ('audio/mpeg|play', 'MP3 Audio Player'),
    )
    block_type = models.CharField("Block Type",
                                  null=False,
                                  blank=False,
                                  max_length=64,
                                  default='text/md',
                                  choices=BLOCK_TYPE_CHOICES,
                                  help_text="Choose what this block will do, then use those settings in the expanding menus below.")


    class Meta:
        ordering = ['story__slug','order']

    def get_alt(self):
        if self.image_alt:
            return self.image_alt
        elif self.image_caption:
            return self.image_caption
        else:
            return None

    def __str__(self):
        return "%s in %s" % (self.id, self.story.name)
