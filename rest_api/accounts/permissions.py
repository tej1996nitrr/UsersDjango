from rest_framework import permissions


class IsProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print("req",request.user)
        print("obj",obj.username)

        return obj.username == request.user



