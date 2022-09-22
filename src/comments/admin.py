from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):

    model = Comment
    list_display = ("description_comment", "created_at", "updated_at")


admin.site.register(Comment, CommentAdmin)
