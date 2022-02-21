

from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allows user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allows users to only update their own ststus"""

    def has_object_permission(self, request, view, obj):
        """Checks if user is trying to edit thier own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
