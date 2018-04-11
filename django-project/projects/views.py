# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from.models import Project, Story, Block
from bakery.views import BuildableDetailView

# Create your views here.
class StoryDetailView(BuildableDetailView):
    model = Story
    template_name = 'projects/story_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Story.objects.get(slug=self.kwargs['slug'])
        return super(StoryDetailView, self).get_objects()

class ProjectHTMLView(BuildableDetailView):
    model = Project
    template_name = 'projects/project_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Project.objects.get(slug=self.kwargs['slug'])
        return super(StoryDetailView, self).get_objects()
