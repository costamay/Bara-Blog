
from django.contrib import admin
from django.urls import path, include
from posts.views import login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/login/', login_view ),
    path('accounts/register/', register_view),
    path('accounts/logout/', logout_view),
]
