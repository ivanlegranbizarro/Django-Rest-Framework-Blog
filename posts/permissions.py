from rest_framework.permissions import BasePermission


class IsAdminOrAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return True
        return request.user.is_staff or request.user == obj.author
