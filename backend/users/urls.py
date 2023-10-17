from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ViewSetForUsers

app_name = 'users'

router = DefaultRouter()

router.register('users', ViewSetForUsers)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
