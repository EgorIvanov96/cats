from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, PorodeViewSet, CatsViewSet

app_name = 'api'

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('porode', PorodeViewSet, basename='porode')
router.register('cats', CatsViewSet, basename='cats')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.jwt')),
]
