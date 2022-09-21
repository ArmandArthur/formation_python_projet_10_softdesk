from django.contrib import admin
from .models import Issue


class IssueAdmin(admin.ModelAdmin):

    model = Issue
    list_display = ('title_issue', 'created_at', 'updated_at')

admin.site.register(Issue, IssueAdmin)
