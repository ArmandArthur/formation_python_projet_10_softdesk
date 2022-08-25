from rest_framework.permissions import BasePermission
from projects.models import Contributor

class ProjectPermission(BasePermission):
    def has_permission(self, request, view):
        if 'pk' in view.kwargs:
            project_id = view.kwargs['pk']
            if request.method == 'DELETE':
                is_contributor = Contributor.objects.filter(project=project_id, user=request.user.id, role='Author').exists()
            else:
                is_contributor = Contributor.objects.filter(project=project_id, user=request.user.id).exists()
        else:
            is_contributor = True

        if is_contributor:
            return True
        return False
