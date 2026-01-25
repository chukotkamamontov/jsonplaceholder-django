from django.shortcuts import render
from django.http import JsonResponse
from .models import User

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