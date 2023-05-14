from flask import session
from flask_login import current_user
from ez2erp import CONTEXT
from ez2erp.core.models import Model



def load_permissions(user_id):
    from ez2erp.auth.models import User, UserPermission, RolePermission
    user = User.query.retrieve(user_id)

    if not user and not current_user.is_authenticated:
        CONTEXT['system_modules'].pop('admin',None)
        return True

    session.pop('permissions', None)
    if "permissions" not in session:
        session['permissions'] = {}

    print(user.role)

    if user.is_superuser:
        all_permissions = Model.query.all()
        print("all_permissions:", all_permissions)
        for permission in all_permissions:
            session['permissions'][permission.name] = {"read": True, "create": True, \
                "write": True, "delete": True}  
    
    elif user.role.name == "Individual" or user.role_id == 1:
        # TODO: GAMITIN ANG user.permissions kaysa mag query pa ulit
        user_permissions = UserPermission.query.filter_by(user_id=user_id)
        for user_permission in user_permissions:
            session['permissions'][user_permission.model.name] = {"read": user_permission.read, "create": user_permission.create, \
                "write": user_permission.write, "delete": user_permission.delete}
    else:
        role_permissions = RolePermission.query.filter_by(role_id=user.role_id)
        for role_permission in role_permissions:
            session['permissions'][role_permission.model.name] = {"read": role_permission.read, "create": role_permission.create, \
                "write": role_permission.write, "delete": role_permission.delete}
    return True


def check_create(model_name):
    from ez2erp.auth.models import User

    if current_user.is_superuser:
        return True
        
    user = User.query.get(current_user.id)
    
    for perm in user.permissions:
    
        if model_name == perm.model.name:
    
            if perm.create:
                return True
            else:
                return False

    return False


def check_read(model_name):
    from ez2erp.auth.models import User

    if current_user.is_superuser:
        return True
    
    user = User.query.get(current_user.id)
    
    for perm in user.permissions:
        
        if model_name == perm.model.name:
        
            if perm.read:
                return True
            else:
                return False

    return False