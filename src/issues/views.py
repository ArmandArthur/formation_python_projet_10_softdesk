from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Issue
from .permissions import IssuePermission
from .serializers import IssueSerializer
from rest_framework import status
from rest_framework.response import Response


class IssueViewSet(viewsets.ModelViewSet):

    serializer_class = IssueSerializer
    http_method_names = ['get', 'post','put','delete']
    permission_classes = (IsAuthenticated, IssuePermission)

    def get_queryset(self):
        return Issue.objects.all()
    
    def create(self, request, *args, **kwargs):
        _mutable = request.data._mutable
        request.data._mutable = True
        request.data['project'] = kwargs['projects_pk']
        request.data['author'] = request.user.id
        request.data._mutable = _mutable
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        issue_instance = Issue.objects.filter(id=kwargs['pk']).first()
        serializer = IssueSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(issue_instance,  serializer.validated_data)
        serializer_data = serializer.validated_data
        serializer_data['project'] = kwargs['projects_pk']
        serializer_data['author'] = issue_instance.author.id
        return Response(serializer_data, status=status.HTTP_201_CREATED)
        
    def list(self, request, *args, **kwargs):
        project_id = kwargs['projects_pk']
        issues = Issue.objects.filter(project_id=project_id)
        serializer = IssueSerializer(issues, many=True)
        return Response({'issues': serializer.data}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        return super(IssueViewSet, self).destroy(request,args, **kwargs)
