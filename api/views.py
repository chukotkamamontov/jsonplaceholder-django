from django.shortcuts import render

from django.http import JsonResponse
from .models import User, Post, Comment

def model_to_dict(instance, fields=None):
    """
    Универсальная функция для превращения Django модели в dict

    Пример SQL:
    Тут SQL нет — это просто работа с уже загруженным объектом
    """
    data = {}
    for field in instance._meta.fields:
        name = field.name
        if fields and name not in fields:
            continue
        value = getattr(instance, name)
        # Если это ForeignKey — берем id связанной записи
        if hasattr(value, "id"):
            value = value.id
        data[name] = value
    return data

# =====================================================
# GET /users/
# =====================================================
def users_list(request):
    """
    SQL:
        SELECT
            id,
            name,
            email
        FROM api_user;

        или SELECT * FROM api_user;
    """

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

# =====================================================
# GET /posts/
# =====================================================
def posts_list(request):
    """
    SQL (примерно):
        SELECT
            id,
            user_id,
            title,
            body
        FROM api_post;
    """
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


# =====================================================
# GET /posts/<id>/
# =====================================================
def post_detail(request, post_id):
    try:
        """
        SQL:
            SELECT
                id,
                user_id,
                title,
                body
            FROM api_post
            WHERE id = 5
            LIMIT 1;
        """
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


# =====================================================
# GET /comments/
# GET /comments/?postId=1
# =====================================================
def comments_list(request):
    """
    без фильтра:
        GET /comments/

    SQL (примерно):
        SELECT
            id,
            post_id,
            name,
            email,
            body
        FROM api_comment;


    с фильтром:
        GET /comments/?postId=1

    SQL (примерно):
        SELECT
            id,
            post_id,
            name,
            email,
            body
        FROM api_comment
        WHERE post_id = 1;
    """
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