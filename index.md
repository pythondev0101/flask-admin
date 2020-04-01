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
