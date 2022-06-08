from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('title_project',)

admin.site.register(Project, ProjectAdmin)
