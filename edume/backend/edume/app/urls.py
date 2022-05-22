from django.urls import path
from . import views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
                  path('', views.main, name='main'),
                  path('user/new/', views.user_new, name='user_new'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
