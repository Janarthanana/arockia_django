
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="register"),
    path('registerpath/', views.register, name="registerpath"),
    path('login/', views.loginfirst, name="loginapp"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
