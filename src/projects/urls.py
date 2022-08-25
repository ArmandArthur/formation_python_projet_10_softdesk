from django.urls import include, path
from rest_framework_nested import routers
from . import views

projects_router = routers.SimpleRouter(trailing_slash=False)
projects_router.register("projects/?", views.ProjectViewSet, basename='Project')

user_router = routers.NestedSimpleRouter(projects_router, r'projects/?', lookup='projects', trailing_slash=False)
user_router.register(r"users/?", views.ProjectContributorViewSet, basename='Contributor')

urlpatterns = [
    path("", include(projects_router.urls)),
    path("", include(user_router.urls))
]