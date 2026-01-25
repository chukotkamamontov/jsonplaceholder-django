from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('users/', csrf_exempt(views.user_list), name='user_list'),
    path('users/create/', csrf_exempt(views.user_create), name='user_create'),
    path('users/<int:pk>/', csrf_exempt(views.user_detail), name='user_detail'),
    path('users/<int:pk>/update/', csrf_exempt(views.user_update), name='user_update'),
    path('users/<int:pk>/delete/', csrf_exempt(views.user_delete), name='user_delete'),
]