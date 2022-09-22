from rest_framework.permissions import BasePermission
from .models import Comment
from projects.models import Contributor


class CommentPermission(BasePermission):
    def has_permission(self, request, view):
        is_author = False
        if "pk" in view.kwargs:
            comment_id = view.kwargs["pk"]
            if request.method == "DELETE" or request.method == "PUT":
                is_author = Comment.objects.filter(
                    id=comment_id, author=request.user.id
                ).exists()
            # GET pour get comment avec pk (single)
            elif request.method == "GET":
                project_id = view.kwargs["projects_pk"]
                is_contributor = Contributor.objects.filter(
                    project=project_id, user=request.user.id
                ).exists()
                is_author = is_contributor
        # GET pour comment sans pk (liste)
        elif request.method == "POST" or request.method == "GET":
            project_id = view.kwargs["projects_pk"]
            is_contributor = Contributor.objects.filter(
                project=project_id, user=request.user.id
            ).exists()
            is_author = is_contributor
        else:
            is_author = True
        return is_author
