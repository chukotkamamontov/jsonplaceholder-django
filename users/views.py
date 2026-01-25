import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User


# =====================
# Список пользователей
# =====================
def user_list(request):
    users = list(User.objects.values())
    return JsonResponse(users, safe=False)


# =====================
# Создание пользователя
# =====================
@csrf_exempt
def user_create(request):
    data = json.loads(request.body)

    user = User(
        username=data.get('username', ''),
        name=data.get('name', ''),
        email=data.get('email', ''),
        is_staff=data.get('is_staff', False)
    )

    # Устанавливаем пароль правильно
    user.set_password(data.get('password', ''))

    user.save()

    return JsonResponse({'id': user.id, 'username': user.username, 'name': user.name})


# =====================
# Просмотр одного пользователя
# =====================
@csrf_exempt
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    return JsonResponse({
        'id': user.id,
        'username': user.username,
        'name': user.name,
        'email': user.email,
        'is_staff': user.is_staff,
    })


# =====================
# Обновление пользователя
# =====================
@csrf_exempt
def user_update(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    data = json.loads(request.body)
    user.username = data.get('username', user.username)
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    user.is_staff = data.get('is_staff', user.is_staff)
    user.save()
    return JsonResponse({'message': 'User updated'})


# =====================
# Удаление пользователя
# =====================
@csrf_exempt
def user_delete(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    user.delete()
    return JsonResponse({'message': 'User deleted'})