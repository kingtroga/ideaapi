from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticated users can only see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to author of a post
        return obj.author == request.user.user_id

class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False