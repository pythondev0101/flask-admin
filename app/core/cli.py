import platform
import os
import click
import csv
from shutil import copyfile
from config import basedir
from app.core.models import HomeBestModel,HomeBestModule
from app import CONTEXT, MODULES, SYSTEM_MODULES
from app import db
from . import bp_core
from .models import CoreCity,CoreProvince
from app.auth.models import User, Role


@bp_core.cli.command('create_superuser')
def create_superuser():
    _create_superuser()


@bp_core.cli.command("create_module")
@click.argument("module_name")
def create_module(module_name):
    try:

        if platform.system() == "Windows":
            module_path = basedir + "\\app" + "\\" + module_name
            templates_path = basedir + "\\app" + "\\" + module_name + "\\" + "templates" + "\\" + module_name 
            core_init_path = basedir + "\\app" + "\\core" + \
                "\\module_template" + "\\__init__.py"
            core_models_path = basedir + "\\app" + \
                "\\core" + "\\module_template" + "\\models.py"
            core_routes_path = basedir + "\\app" + \
                "\\core" + "\\module_template" + "\\routes.py"
        elif platform.system() == "Linux":
            module_path = basedir + "/app" + "/" + module_name
            templates_path = basedir + "/app" + "/" + module_name + "/templates" + "/" + module_name
            core_init_path = basedir + "/app" + "/core" + "/module_template" + "/__init__.py"
            core_models_path = basedir + "/app" + "/core" + "/module_template" + "/models.py"
            core_routes_path = basedir + "/app" + "/core" + "/module_template" + "/routes.py"

        core_file_list = [core_init_path, core_models_path, core_routes_path]

        if not os.path.exists(module_path):
            os.mkdir(module_path)
            os.makedirs(templates_path)
            for file_path in core_file_list:
                file_name = os.path.basename(file_path)
                copyfile(file_path, os.path.join(module_path, file_name))
    except OSError as e:
        print("Creation of the directory %s failed" % module_path)
        print(e)
    else:
        print("Successfully created the directory %s " % module_path)


@bp_core.cli.command("install")
def install():
    """
    Tatanggap to ng list ng modules tapos iinsert nya sa database yung mga models o tables nila, \
        para malaman ng system kung ano yung mga models(eg. Users,Customers)
    Parameters
    ----------
    modules
        Listahan ng mga modules na iinstall sa system
    """




    print("Installing...")

    if platform.system() == "Windows":
        provinces_path = basedir + "\\app" + "\\core" + "\\csv" + "\\provinces.csv"
        cities_path = basedir + "\\app" + "\\core" + "\\csv" + "\\cities.csv"
    elif platform.system() == "Linux":
        provinces_path = basedir + "/app/core/csv/provinces.csv"
        cities_path = basedir + "/app/core/csv/cities.csv"
    else:
        raise Exception("Platform not supported yet.")

    db.create_all()
    db.session.commit()
    
    module_count = 0

    for module in MODULES:
        SYSTEM_MODULES.append({'name':module.module_name,'short_description': module.module_short_description,
        'long_description':module.module_long_description,'link': module.module_link,
        'icon': module.module_icon, 'models': []})
        
        # TODO: Iimprove to kasi kapag nag error ang isa damay lahat dahil sa last_id
        homebest_module = HomeBestModule.query.filter_by(name=module.module_name).first()
        last_id = 0
        if not homebest_module:
            new_module = HomeBestModule(module.module_name,module.module_short_description,module.version)
            new_module.long_description = module.module_long_description
            new_module.status = 'installed'
            db.session.add(new_module)
            db.session.commit()
            print("MODULE - {}: SUCCESS".format(new_module.name))
            last_id = new_module.id

        model_count = 0

        for model in module.models:
            homebestmodel = HomeBestModel.query.filter_by(name=model.__amname__).first()
            if not homebestmodel:
                new_model = HomeBestModel(model.__amname__, last_id, model.__amdescription__)
                db.session.add(new_model)
                db.session.commit()
                print("MODEL - {}: SUCCESS".format(new_model.name))
            SYSTEM_MODULES[module_count]['models'].append({'name':model.__amname__,'description':model.__amdescription__,\
                'icon': model.__amicon__, 'functions': []})
            
            for function in model.__amfunctions__:
                for function_name, function_link in function.items():
                    SYSTEM_MODULES[module_count]['models'][model_count]['functions'].append({
                        function_name:function_link
                    })
        
            model_count = model_count + 1

        if len(module.no_admin_models) > 0 :

            for xmodel in module.no_admin_models:
                homebestmodel = HomeBestModel.query.filter_by(name=xmodel.__amname__).first()
                if not homebestmodel:
                    new_model = HomeBestModel(xmodel.__amname__, last_id, xmodel.__amdescription__,False)
                    db.session.add(new_model)
                    db.session.commit()
                    print("MODEL - {}: SUCCESS".format(new_model.name))

        module_count = module_count + 1

    print("Inserting provinces to database...")
    if CoreProvince.query.count() < 88:
        with open(provinces_path) as f:
            csv_file = csv.reader(f)
            for id, row in enumerate(csv_file):
                if not id == 0:
                    province = CoreProvince()
                    province.id = int(row[0])
                    province.name = row[2]
                    db.session.add(province)
            db.session.commit()
        print("Provinces done!")
    else:
        print("Provinces exists!")
    print("")
    print("Inserting cities to database...")
    if CoreCity.query.count() < 1647:
        with open(cities_path) as f:
            csv_file = csv.reader(f)
            for id,row in enumerate(csv_file):
                if not id == 0:
                    city = CoreCity()
                    city.id = int(row[0])
                    city.name = row[2]
                    city.province_id = None
                    db.session.add(city)
            db.session.commit()
        print("Cities done!")
    else:
        print("Cities exists!")

    print("Inserting system roles...")
    if Role.query.count() > 0:
        print("Role already inserted!")
    else:
        role = Role()
        role.name = "Individual"
        db.session.add(role)
        db.session.commit()
        print("Individual role inserted!")

    if not User.query.count() > 0:
        print("Creating a SuperUser/owner...")
        _create_superuser()

    print("Installation complete!")


def _create_superuser():
    try:
        user = User()
        user.fname = "Administrator"
        user.lname = "Administrator"
        user.username = input("Enter Username: ")
        user.email = None
        user.set_password(input("Enter password: "))
        user.is_superuser = 1
        user.role_id = 1
        user.created_by = "System"	
        db.session.add(user)
        db.session.commit()
        print("SuperUser Created!")
    except Exception as exc:
        print(str(exc))
