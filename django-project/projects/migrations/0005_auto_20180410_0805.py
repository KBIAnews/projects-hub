# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20180409_1523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'ordering': ['story__slug', 'order']},
        ),
        migrations.AddField(
            model_name='block',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to=b'', verbose_name='Audio MP3 Upload'),
        ),
        migrations.AddField(
            model_name='block',
            name='block_type',
            field=models.CharField(choices=[('text/md', 'Markdown Formatted Text'), ('text/html', 'HTML Formatted Text'), ('image/*|full', 'Full Width Image'), ('audio/mpeg|play', 'MP3 Audio Player')], default='text/md', help_text='Choose what this block will do, then use those settings in the expanding menus below.', max_length=64, verbose_name='Block Type'),
        ),
        migrations.AddField(
            model_name='block',
            name='image_alt',
            field=models.CharField(blank=True, help_text='Alternate image text for screen readers and SEO. If you do not specify, this falls back to image caption.', max_length=1024, null=True, verbose_name="Image 'Alt Text'"),
        ),
        migrations.AddField(
            model_name='block',
            name='image_caption',
            field=models.TextField(blank=True, null=True, verbose_name='Image Caption'),
        ),
        migrations.AddField(
            model_name='block',
            name='image_credit',
            field=models.CharField(blank=True, max_length=280, null=True, verbose_name='Image Credit'),
        ),
        migrations.AddField(
            model_name='block',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Image Upload'),
        ),
        migrations.AlterField(
            model_name='block',
            name='id',
            field=models.CharField(default=projects.models.pkgen, max_length=10, primary_key=True, serialize=False, verbose_name='Internal CMS ID'),
        ),
    ]