from djoser.views import UserViewSet
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response


from users.models import User
from reviews.models import Porode, Cats
from .serializers import (
    UserCastomSerializer, PorodeSerializer,
    CatsSerializer, CatsListSerializer)
from .filters import CatsFilter
from .permission import IsAuthorOrReadOnly


class UserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserCastomSerializer


class PorodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Porode.objects.all()
    serializer_class = PorodeSerializer


class CatsViewSet(viewsets.ModelViewSet):
    queryset = Cats.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CatsFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return CatsListSerializer
        return CatsSerializer

    def update(self, request, *args, **kwargs):
        cats = self.get_object()
        if cats.owner != request.user:
            return Response(
                'Вы не можете вносить изменения в чужую публикацию❗❗❗',
                status=status.HTTP_400_BAD_REQUEST)
        return Response('Вы изменили свою публикацию!',
                        status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        cats = self.get_object()
        if cats.owner != request.user:
            return Response(
                'Вы не можете удалить чужую публикацию❗❗❗',
                status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(cats)
        return Response('Вы удалили свою публикацию!',
                        status=status.HTTP_204_NO_CONTENT)
