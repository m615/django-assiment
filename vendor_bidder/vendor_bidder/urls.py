
from django.contrib import admin
from django.urls import path, re_path, include
from accounts.views import (
    login_view,
    logout_view,
    register_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    re_path(r'profile?/', include('profiles.urls')),
    re_path(r'api/profile?/', include('profiles.api.urls')),
]
