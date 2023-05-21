from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # So basically, here we augment our authorization system
    # so then a staff user has to have 'view' permission
    # on our product model to be able to view (list or retrieve) product
    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }

    # def has_permission(self, request, view):
    #     # Technically; we do not need to do this verification
    #     # because there is a builtin permission for that (IsAdminUser)
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)
