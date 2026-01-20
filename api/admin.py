from django.contrib import admin

from .models import User, Post, Comment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    search_fields = ("name", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user")
    list_filter = ("user",)
    search_fields = ("title", "body")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "email")
    list_filter = ("post",)
    search_fields = ("name", "email", "body")
