from rest_framework import permissions

class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        if method.request in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.views_genre')
        
        if method.request == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        return False