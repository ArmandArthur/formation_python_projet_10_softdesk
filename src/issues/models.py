from django.db import models
from django.conf import settings
from projects.models import Project


class Issue(models.Model):
    title_issue = models.CharField(max_length=128)
    description_issue = models.CharField(max_length=128)
    tag_issue = models.CharField(max_length=128)
    priority_issue = models.CharField(max_length=128)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    status_issue = models.CharField(max_length=128)

    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_issue

    class Meta:
        db_table = 'issues'
