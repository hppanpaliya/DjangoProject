from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello_world),
    path("login/", views.login),
    path("signup/", views.signup),
    path('users/', views.get_all_users),
    path('users/<str:email>/', views.user_operations),
]
