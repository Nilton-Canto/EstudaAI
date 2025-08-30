
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logins.urls')), # URL Login
    path('logins/', include('django.contrib.auth.urls')), # URL Login
]
