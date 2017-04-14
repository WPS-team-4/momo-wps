from rest_framework import permissions
from rest_framework.permissions import BasePermission

__all__ = (
    'IsOwnerOrReadOnly',
)


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
