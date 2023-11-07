from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit its own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit its own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to edit only its own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to edit its own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile == request.user.id
