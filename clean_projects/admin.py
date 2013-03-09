from clean_projects.models import Project, Subject, Sketch
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class SketchAdmin(admin.ModelAdmin):
    pass

class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Project,ProjectAdmin)
admin.site.register(Sketch,SketchAdmin)
admin.site.register(Subject,SubjectAdmin)
