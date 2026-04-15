# rbac_model.py

"""
Definition: Role-Based Access Control (RBAC) is an approach to restricting system access to authorized users based on their roles within an organization.
"""

class RBAC:
    def __init__(self):
        self.roles = {
            "admin": ["create", "read", "update", "delete"],
            "editor": ["read", "update"],
            "viewer": ["read"]
        }
        self.user_roles = {}

    def assign_role(self, user, role):
        self.user_roles[user] = role

    def check_permission(self, user, permission):
        role = self.user_roles.get(user)
        if role and permission in self.roles.get(role, []):
            return True
        return False

# Usage
rbac = RBAC()
rbac.assign_role("kunal", "admin")
rbac.assign_role("guest", "viewer")

print(f"Kunal can delete? {rbac.check_permission('kunal', 'delete')}")
print(f"Guest can delete? {rbac.check_permission('guest', 'delete')}")
