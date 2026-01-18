from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.users_list),
    path("posts/", views.posts_list),
    path("posts/<int:post_id>/", views.post_detail),
    path("comments/", views.comments_list),
]