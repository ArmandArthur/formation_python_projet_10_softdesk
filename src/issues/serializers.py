from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):

    title_issue = serializers.CharField(max_length=128, min_length=4)
    description_issue = serializers.CharField(max_length=128, min_length=4)
    tag_issue = serializers.CharField(max_length=128, min_length=2)
    priority_issue = serializers.CharField(max_length=128, min_length=1)
    status_issue = serializers.CharField(max_length=128, min_length=2)

    class Meta:
        model = Issue
        fields = [
            "id",
            "title_issue",
            "description_issue",
            "tag_issue",
            "priority_issue",
            "status_issue",
            "project",
            "author",
        ]
