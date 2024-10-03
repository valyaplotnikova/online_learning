from rest_framework import permissions


class IsModers(permissions.BasePermission):
    """ Проверяет, является ли пользователь Модератором. """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()


class IsOwner(permissions.BasePermission):
    """ Проверяет, является ли пользователь владельцем. """
    def has_object_permission(self, request, view, obj):

        if obj.owner == request.user:
            return True
        return False
