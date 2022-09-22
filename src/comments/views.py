from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .permissions import CommentPermission
from .serializers import CommentSerializer
from rest_framework import status
from rest_framework.response import Response


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = (IsAuthenticated, CommentPermission)

    def get_queryset(self):
        return Comment.objects.all()

    def create(self, request, *args, **kwargs):
        _mutable = request.data._mutable
        request.data._mutable = True
        request.data["issue"] = kwargs["issues_pk"]
        request.data["author"] = request.user.id
        request.data._mutable = _mutable
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        commment_instance = Comment.objects.filter(id=kwargs["pk"]).first()
        serializer = CommentSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(commment_instance, serializer.validated_data)
        serializer_data = serializer.validated_data
        serializer_data["issue"] = kwargs["issues_pk"]
        serializer_data["author"] = commment_instance.author.id
        return Response(serializer_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        issue_id = kwargs["issues_pk"]
        comments = Comment.objects.filter(issue_id=issue_id)
        serializer = CommentSerializer(comments, many=True)
        return Response({"issues": serializer.data}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        comment_id = kwargs["pk"]
        comment = Comment.objects.filter(id=comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        return super(CommentViewSet, self).destroy(request, args, **kwargs)
