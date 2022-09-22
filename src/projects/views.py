from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project, Contributor
from .permissions import ProjectPermission, ProjectContributorPermission
from users.models import CustomUser
from .serializers import (
    ProjectSerializer,
    ProjectContributorSerializer,
    ProjectContributorCrudSerializer,
)
from rest_framework import status
from rest_framework.response import Response


class ProjectContributorViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectContributorCrudSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = (IsAuthenticated, ProjectContributorPermission)

    def create(self, request, *args, **kwargs):
        data_contrib = {}
        data_contrib["project_id"] = kwargs["projects_pk"]
        data_contrib["user_id"] = request.data["user_id"]
        data_contrib["role"] = "Contributor"
        serializer_contrib = ProjectContributorCrudSerializer(data=data_contrib)
        if serializer_contrib.is_valid():
            serializer_contrib.save()
            serializer_data = serializer_contrib.data
            return Response(serializer_data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer_contrib.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        user_id = kwargs["pk"]
        contrib_del = Contributor.objects.filter(user=user_id, role="Contributor")
        contrib_del.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        project_id = kwargs["projects_pk"]
        contributors = Contributor.objects.filter(project_id=project_id)
        serializer = ProjectContributorSerializer(contributors, many=True)
        return Response({"contributors": serializer.data}, status=status.HTTP_200_OK)


class ProjectViewSet(viewsets.ModelViewSet, ProjectPermission):
    serializer_class = ProjectSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [ProjectPermission]

    def get_user(self, user_id):
        user = CustomUser.objects.filter(id=user_id).values("id", "email").first()
        return user

    def get_queryset(self):
        return Project.objects.all()

    def list(self, request, *args, **kwargs):
        user_id = request.data["user_id"]
        # used related_name "users"
        projects = Project.objects.filter(users=user_id)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            if "id" in serializer_data:
                data_contrib = {}
                data_contrib["project_id"] = serializer.data["id"]
                data_contrib["user_id"] = request.user.id
                data_contrib["role"] = "Author"
                serializer_contrib = ProjectContributorCrudSerializer(data=data_contrib)
                if serializer_contrib.is_valid():
                    serializer_contrib.save()
                    serializer_data["user"] = self.get_user(
                        serializer_contrib.data["user_id"]
                    )
            return Response(serializer_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return super(ProjectViewSet, self).update(request, args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        project_id = project.id
        contrib_join = Contributor.objects.filter(project=project_id)
        contrib_join.delete()
        return super(ProjectViewSet, self).destroy(request, args, **kwargs)
