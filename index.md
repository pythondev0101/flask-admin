# HomeBest Framework - Version 1

## Features

* Ready to use application
* Fast and secured 
* Built-in modules and models:
    - Authentication : User
    - Admin: Dashboard
    - Core: Index, and Command line arguments
* Easy to modify 

## Built-in Models (Your common project models)
Don't create customers table or addresses table from scratch anymore, you will just implement then its good to go!!!
Sample code to implement built-in models in your module
```python
from app.core.models import CoreCustomer, Base # Import the built-in models

class Customer(CoreCustomer) # Inherit built-in model to your class to implement
    __tablename__ = 'table_name'
    # Include here your fields
```
Its super easy!!!

## homebest.py Command Line arguments
To create a superuser or owner of the system type the ff:
```shell
$ python homebest.py - create_superuser
```
To create a module of the system type the ff:
```shell
$ python homebest.py - create_module {module name}
```
## Your Module code
In your module folder(eg.homebest/module_ko)
Create your __init__.py then type the ff:
```python
from flask import Blueprint

# URLS DICTIONARY
module_ko_urls = {
    'index': 'bp_module_ko.index',
}

bp_module_ko = Blueprint('bp_module_ko', __name__)

@bp_core.route('/module_ko')
def index():
    return "HELLO WORLD"
```
Note: Just one file you have a running system and module, that's super easy!!!!

## Installation
To install just clone the repository or download
To clone type the ff:
```shell
$ git clone -b {version} git@github.com:pythondev0101/homebest-framework.git
```

## Updates

To update type the ff:

```shell
$ git pull origin {version}
```

# Documentation

### Creating a Module

1. Go to homebest folder
2. To create module folder and files, type the ff:
```shell
$ python homebest.py --create_module {module_name}
```
3. Go to the generated module folder in homebest/app/{module_name}
4. Open and modify __init__.py
```python
from flask import Blueprint
from app import system_modules

bp_module = Blueprint('bp_module', __name__,)

blueprint_name = ""  # The name of the module's blueprint
module_name = "" # The name of the module

"""URLS DICTIONARY"""
NOTE: CHANGE (model) to your module's model eg. customer_create
module_urls = {
    'index': '{}.index'.format(blueprint_name),
    'create': '{}.(model)_create'.format(blueprint_name),
    'edit': '{}.(model)_edit'.format(blueprint_name),
    'delete': '{}.(model)_delete'.format(blueprint_name),
}

"""TEMPLATES DICTIONARY"""
"""NOTE: CHANGE (model) to your module's model eg. customer_create.html"""
module_templates = {
    'index': '{}/(model)_index.html'.format(module_name),
    'create': '{}/(model)_create.html'.format(module_name),
    'edit': '{}/(model)_.html'.format(module_name),
}

from . import routes
from . import models

""" THIS IS FOR ADMIN MODELS """

class UserModel():
    model_name= 'Users'
    model_icon = 'fa-users'
    functions = {'View users': 'bp_auth.index'}

class AdminModule():
    module_name = 'admin'
    module_icon = 'fa-home'
    module_link = 'bp_admin.index'
    module_description = 'Administrator'
    models = [UserModel]
```
NOTE: Change {module} to your module's name
NOTE: Change AdminModule() and UserModel() to your preferred class names and modify their attributes
5. Open and modify routes.py and models.py of your module
6. It's time to include and register your module to app/__init__.py
7. Open and update/modify app/__init__.py
8. In app.app_context(): import your module there, sample...
```python
        """EDITABLE: IMPORT HERE THE SYSTEM MODULES  """
        from app import core
        from app import auth
        from app import admin
        from app import your_module
        """--------------END--------------"""
```
```python
        """EDITABLE: INCLUDE HERE YOUR MODULE Admin models FOR ADMIN TEMPLATE"""
        modules = [admin.AdminModule, your_module.Module]
        """--------------END--------------"""
```
```python
        """EDITABLE: REGISTER HERE THE MODULE BLUEPRINTS"""
        app.register_blueprint(core.bp_core, url_prefix='/')
        app.register_blueprint(auth.bp_auth, url_prefix='/auth')
        app.register_blueprint(admin.bp_admin, url_prefix='/admin')
        app.register_blueprint(your_module.bp_module, url_prefix='/your_url_module')
        """--------------END--------------"""
```
9. Then save the file.
10. Your module is ready to use now, to run the system type the ff:
```shell
$ flask run
```
