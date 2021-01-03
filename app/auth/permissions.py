from flask import session
from flask_login import current_user
from app import CONTEXT, MODULES
from app.auth.models import User, UserPermission, RolePermission
from app.core.models import CoreModel



def check_create(model_name):
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


def load_permissions(user_id):
    user = User.query.get(user_id)
    module_count = 0

    system_modules = []

    for module in MODULES:
        system_modules.append({'name':module.module_name,'short_description': module.module_short_description,
        'long_description':module.module_long_description,'link': module.module_link,
        'icon': module.module_icon, 'models': []})

        model_count = 0

        for model in module.models:

            system_modules[module_count]['models'].append({'name':model.__amname__,'description':model.__amdescription__,\
                'icon': model.__amicon__, 'functions': [], 'list_view_url':model.__list_view_url__})
            
            for function in model.__amfunctions__:
                for function_name, function_link in function.items():
                    system_modules[module_count]['models'][model_count]['functions'].append({
                        function_name:function_link
                    })
        
            model_count = model_count + 1

        module_count = module_count + 1

    CONTEXT['system_modules'] = system_modules

    if not user and not current_user.is_authenticated:
        CONTEXT['system_modules'].pop('admin',None)
    else:
        session.pop('permissions', None)
        if "permissions" not in session:
            session['permissions'] = {}

        if user.is_superuser:
            all_permissions = CoreModel.query.all()
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
