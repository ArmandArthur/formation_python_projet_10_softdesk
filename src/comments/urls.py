from django.urls import include, path
from rest_framework_nested import routers
from . import views
from issues.urls import issue_router

comment_router = routers.NestedSimpleRouter(
    issue_router, r"issues/?", lookup="issues", trailing_slash=False
)
comment_router.register(r"comments/?", views.CommentViewSet, basename="comments")

urlpatterns = [path("", include(comment_router.urls))]
