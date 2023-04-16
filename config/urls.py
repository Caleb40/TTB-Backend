from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('', include(router.urls)),
    path('api/', include('api.urls')),
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.jwt')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
]
