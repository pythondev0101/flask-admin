# HomeBest Framework - Version 1

## Features

* Ready to use application
* Fast and secured 
* Built-in modules and models:
    - Authentication : User
    - Admin: Dashboard
    - Core: Index, and Command line arguments
* Easy to modify 

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
from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user

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
