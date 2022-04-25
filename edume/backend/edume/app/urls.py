from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('user/new/', views.user_new, name='user_new'),
]