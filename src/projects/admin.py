from django.contrib import admin
from .models import Project,Contributor

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('title_project',)

admin.site.register(Project, ProjectAdmin)

class ContributorAdmin(admin.ModelAdmin):
    model = Contributor
    list_display = ('user', 'project','role')

admin.site.register(Contributor, ContributorAdmin)
