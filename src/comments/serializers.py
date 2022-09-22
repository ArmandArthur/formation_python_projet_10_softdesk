from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    description_comment = serializers.CharField(max_length=128, min_length=4)

    class Meta:
        model = Comment
        fields = ["id", "description_comment", "issue", "author"]
