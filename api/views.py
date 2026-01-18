from django.shortcuts import render

from django.http import JsonResponse
from .models import User, Post, Comment

def model_to_dict(instance, fields=None):
    data = {}
    for field in instance._meta.fields:
        name = field.name
        if fields and name not in fields:
            continue
        value = getattr(instance, name)
        if hasattr(value, "id"):
            value = value.id
        data[name] = value
    return data

# /users/
def users_list(request):
    users = User.objects.all()
    data = [
        {
            "id": u.id,
            "name": u.name,
            "email": u.email,
        }
        for u in users
    ]
    return JsonResponse(data, safe=False)

# /posts/
def posts_list(request):
    posts = Post.objects.all()

    data = [
        {
            "id": p.id,
            "userId": p.user_id,
            "title": p.title,
            "body": p.body,
        }
        for p in posts
    ]

    return JsonResponse(data, safe=False)


# /posts/<id>/
def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

    data = {
        "id": post.id,
        "userId": post.user_id,
        "title": post.title,
        "body": post.body,
    }

    return JsonResponse(data)


# /comments/?postId=1
def comments_list(request):
    post_id = request.GET.get("postId")

    comments = Comment.objects.all()
    if post_id:
        comments = comments.filter(post_id=post_id)

    data = [
        {
            "id": c.id,
            "postId": c.post_id,
            "name": c.name,
            "email": c.email,
            "body": c.body,
        }
        for c in comments
    ]

    return JsonResponse(data, safe=False)