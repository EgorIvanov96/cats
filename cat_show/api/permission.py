from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class IsAuthorOrReadOnly(IsAuthenticatedOrReadOnly):
    """Разрешение только автору."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.owner == request.user)
