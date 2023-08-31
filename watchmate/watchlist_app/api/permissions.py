from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        admin_permission = super().has_permission(request, view)
        return request.method == "GET" or admin_permission