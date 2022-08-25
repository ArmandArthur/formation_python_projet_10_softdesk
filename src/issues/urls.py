from django.urls import include, path
from rest_framework_nested import routers
from . import views
from projects.urls import projects_router

issue_router = routers.NestedSimpleRouter(projects_router, r'projects/?', lookup='projects', trailing_slash=False)
issue_router.register(r"issues/?", views.IssueViewSet, basename='Contributor')

urlpatterns = [
    path("", include(issue_router.urls))
]