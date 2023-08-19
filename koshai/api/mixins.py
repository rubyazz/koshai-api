from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class RoleRequiredMixin(UserPassesTestMixin):
    roles_required = []

    def test_func(self):
        user = self.request.user
        if isinstance(user, get_user_model()):
            if any(user.has_role(role) for role in self.roles_required):
                return True
        return False

    def handle_no_permission(self):
        raise PermissionDenied("You do not have permission to access this page.")
