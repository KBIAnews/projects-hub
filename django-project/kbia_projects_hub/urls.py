"""kbia_projects_hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from projects import views as pv


urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^(?P<proj_slug>[\w-]+)/(?P<slug>[\w-]+)/$', pv.StoryDetailView.as_view(),
                      name='storydetail'),
                  # A Couple of Suggested URL Configs
                  # url(r'^kbia_projects_hub/$', HomePageView.as_view()),
                  # url(r'^kbia_projects_hub/posts/(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='posts'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'KBIA Projects Hub Admin'
admin.site.site_title = 'KBIA Projects Hub Admin'