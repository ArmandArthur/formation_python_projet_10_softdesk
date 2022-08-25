from rest_framework import serializers

from users.models import CustomUser
from .models import Project, Contributor


class ProjectSerializer(serializers.ModelSerializer):
    title_project = serializers.CharField(max_length=128, min_length=8)
    description_project = serializers.CharField(max_length=128, min_length=8)
    type_project = serializers.CharField(max_length=128, min_length=4)
    # email_user = serializers.CharField(max_length=128, min_length=4, write_only=True)

    # def create(self, validated_data):
    #     return Project.objects.create(**validated_data)

    class Meta:
        model = Project
        fields = ['id', 'title_project', 'description_project', 'type_project']


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    email = serializers.CharField()
    class Meta:
        fields = ('id', 'email')
        model = CustomUser

class ProjectContributorSerializer(serializers.ModelSerializer):
    project_id = serializers.IntegerField()
    user_full = serializers.SerializerMethodField()
    
    role = serializers.CharField(max_length=128, min_length=4)

    class Meta:
        model = Contributor
        fields = ('project_id', 'role', 'user_full')

    def get_user_full(self, obj):
        customer_account_query = CustomUser.objects.get(
            pk=obj.user_id)
        serializer = CustomUserSerializer(customer_account_query)
        return serializer.data

class ProjectContributorCrudSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    project_id = serializers.IntegerField()

    class Meta:
        model = Contributor
        fields = ('project_id', 'role', 'user_id')

