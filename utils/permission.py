from rest_framework.permissions import BasePermission


class IsNormalUser(BasePermission):
    def has_permission(self, request, view):
        # allow all POST requests
        if not request.user.is_staff:
            if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE' \
                    or request.method == 'PATCH':
                return False


        # Otherwise, only allow authenticated requests
        # Post Django 1.10, 'is_authenticated' is a read-only attribute
        return request.user and request.user.is_authenticated

# # Custom permission for users with "is_active" = True.
# class IsUser(BasePermission):
#     """
#     Allows access only to "user" users.
#     """
#     def has_permission(self, request, view):
#         return request.user and not request.user.is_staff
