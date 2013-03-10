from clean_projects.models import Sketch, Project, Subject
from django.views.generic import *

class ProjectView(DetailView):
    model = Project
    template_name = "project_detail.html"
