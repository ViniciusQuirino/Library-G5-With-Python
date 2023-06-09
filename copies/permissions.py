from rest_framework import permissions


class IsColaborator(permissions.BasePermission):
    def has_object_permission(self, request, obj, pk):
        return request.user.is_authenticated and request.user.is_colaborator
