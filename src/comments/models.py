from django.db import models
from django.conf import settings
from issues.models import Issue


class Comment(models.Model):
    description_comment = models.CharField(max_length=256)

    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description_comment

    class Meta:
        db_table = "comments"
