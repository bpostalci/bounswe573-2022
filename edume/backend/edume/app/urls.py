from django.urls import path
from . import views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
                  path('', views.user_new, name='user_new'),
                  path('user/new/', views.user_new, name='user_new'),
                  path('select_topics/', views.select_topics, name='select_topics'),
                  path('courses/', views.courses, name='courses'),
                  path('course/', views.course, name='course'),
                  path('chapter/', views.chapter, name='chapter'),
                  path('forum/', views.forum, name='forum'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
