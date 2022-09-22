from rest_framework.permissions import BasePermission
from .models import Issue
from projects.models import Contributor


class IssuePermission(BasePermission):
    def has_permission(self, request, view):
        is_author = False
        if "pk" in view.kwargs:
            issue_id = view.kwargs["pk"]
            if request.method == "DELETE" or request.method == "PUT":
                is_author = Issue.objects.filter(
                    id=issue_id, author=request.user.id
                ).exists()
        # GET pour la liste des Issues by project
        elif request.method == "POST" or request.method == "GET":
            project_id = view.kwargs["projects_pk"]
            is_contributor = Contributor.objects.filter(
                project=project_id, user=request.user.id
            ).exists()
            is_author = is_contributor
        else:
            is_author = True
        return is_author
