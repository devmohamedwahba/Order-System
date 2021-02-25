from rest_framework.permissions import BasePermission


class IsNormalUser(BasePermission):
    def has_permission(self, request, view):
        # allow all POST requests
        if not request.user.is_staff:
            if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE' \
                    or request.method == 'PATCH':
                return False

        # Otherwise, only allow authenticated requests
        return request.user and request.user.is_authenticated
