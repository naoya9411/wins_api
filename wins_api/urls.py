from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    # path('api/v1/core/', include('core.urls')),
    # path('api/v1/sns/', include('sns.urls')),
]
