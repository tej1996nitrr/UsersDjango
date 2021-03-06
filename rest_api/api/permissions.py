from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsOwner(BasePermission):
    """ Custom permission class to allow only  owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the  owner."""
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
