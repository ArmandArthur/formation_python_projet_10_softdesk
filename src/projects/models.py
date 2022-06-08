from django.db import models
from django.conf import settings

class Project(models.Model):
    title_project = models.CharField(max_length=128)
    description_project = models.CharField(max_length=128)
    type_project = models.CharField(max_length=128)
    users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, through="users.Contributor", related_name="users")
    
    def __str__(self):
        return self.title_project

    class Meta:
        db_table = 'projects'