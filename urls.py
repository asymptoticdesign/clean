from clean_projects.models import Sketch, Project, Subject
from clean_projects.views import *
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clean.views.home', name='home'),
    # url(r'^clean/', include('clean.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^index/$', TemplateView.as_view(template_name="base.html")),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^browse/$', TemplateView.as_view(template_name="browse.html")),
    url(r'^newproject/$', TemplateView.as_view(template_name="newproject.html")),
    url(r'^projects/$',ListView.as_view(queryset=Project.objects.all(),template_name="projects.html")),
    url(r'^projects/(?P<slug>[-\w]+)/$', DetailView.as_view(model=Project, template_name="project_detail.html")),
    url(r'^projects/sketches/(?P<slug>[-\w]+)/$', DetailView.as_view(model=Sketch, template_name="sketch_detail.html")),
#    url('^sketches/(?P<id_no>[-\w]+)/$', 'django.views.generic.list_detail.object_detail', dict(sketch_dict, id_no='id_no'
)
