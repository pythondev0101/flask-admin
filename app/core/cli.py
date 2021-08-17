import platform
import os
import click
import csv
from shutil import copyfile
from config import basedir
from app.core.models import CoreModel, CoreModule
from app import MODULES
from app import db
from . import bp_core
from .models import CoreCity,CoreProvince
from app.auth.models import User, Role



def core_install():
    """
    Tatanggap to ng list ng modules tapos iinsert nya sa database yung mga models o tables nila, \
        para malaman ng system kung ano yung mga models(eg. Users,Customers)
    Parameters
    ----------
    modules
        Listahan ng mga modules na iinstall sa system
    """

    print("Installing...")

    try:

        if platform.system() == "Windows":
            provinces_path = basedir + "\\app" + "\\core" + "\\csv" + "\\provinces.csv"
            cities_path = basedir + "\\app" + "\\core" + "\\csv" + "\\cities.csv"
        elif platform.system() == "Linux":
            provinces_path = basedir + "/app/core/csv/provinces.csv"
            cities_path = basedir + "/app/core/csv/cities.csv"
        else:
            raise Exception("Platform not supported yet.")
        
        module_count = 0

        homebest_module = None

        for module in MODULES:
            # TODO: Iimprove to kasi kapag nag error ang isa damay lahat dahil sa last_id
            homebest_module = CoreModule.objects(name=module.module_name).first()
            # last_id = 0
            if not homebest_module:
                new_module = CoreModule(
                    name=module.module_name,
                    short_description=module.module_short_description,
                    long_description=module.module_long_description,
                    status='installed',
                    version=module.version
                    ).save()

                homebest_module = new_module
                    
                print("MODULE - {}: SUCCESS".format(new_module.name))
                # last_id = new_module.id

            model_count = 0

            for model in module.models:
                homebestmodel = CoreModel.objects(name=model.__amname__).first()

                if not homebestmodel:
                    new_model = CoreModel(
                        name=model.__amname__,
                        module=homebest_module,
                        description=model.__amdescription__,
                        ).save()

                    print("MODEL - {}: SUCCESS".format(new_model.name))

                model_count = model_count + 1

            if len(module.no_admin_models) > 0 :

                for xmodel in module.no_admin_models:
                    homebestmodel = CoreModel.objects(name=xmodel.__amname__).first()
                    
                    if not homebestmodel:
                        new_model = CoreModel(
                            name=xmodel.__amname__, 
                            module=homebest_module,
                            description=xmodel.__amdescription__,
                            admin_included=False
                        ).save()

                        print("MODEL - {}: SUCCESS".format(new_model.name))

            module_count = module_count + 1

        print("Inserting provinces to database...")
        if CoreProvince.objects.count() < 88:
            with open(provinces_path) as f:
                csv_file = csv.reader(f)

                for id, row in enumerate(csv_file):
                    if not id == 0:
                        CoreProvince(
                            name=row[2]
                        ).save()

            print("Provinces done!")

        else:
            print("Provinces exists!")
        print("")
        print("Inserting cities to database...")
        
        if CoreCity.objects.count() < 1647:
            with open(cities_path) as f:
                csv_file = csv.reader(f)

                for id,row in enumerate(csv_file):
                    if not id == 0:
                        
                        CoreCity(
                            name=row[2]
                        ).save()

            print("Cities done!")
        else:
            print("Cities exists!")

        print("Inserting system roles...")
        if Role.objects.count() > 0:
            print("Role already inserted!")
        else:
            Role(
                name="Individual",
            ).save()
            
            print("Individual role inserted!")

        if not User.objects.count() > 0:
            print("Creating a SuperUser/owner...")
            _create_superuser()

    except Exception as exc:
        print(str(exc))
        return False

    return True


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
        else:
            raise Exception
        
        core_file_list = [core_init_path, core_models_path, core_routes_path]

        if not os.path.exists(module_path):
            os.mkdir(module_path)
            os.makedirs(templates_path)
            for file_path in core_file_list:
                file_name = os.path.basename(file_path)
                copyfile(file_path, os.path.join(module_path, file_name))
    except OSError as e:
        print("Creation of the directory failed")
        print(e)
    else:
        print("Successfully created the directory %s " % module_path)


@bp_core.cli.command("install")
def install():

    if core_install():
        print("Installation complete!")

    else:
        print("Installation failed!")


def _create_superuser():
    try:
        role = Role.objects(name="Individual").first()

        user = User(
            fname="Administrator",
            lname="Administrator",
            username = input("Enter Username: "),
            email = None,
            is_superuser = 1,
            role=role,
            created_by = "System",
        )
        user.set_password(input("Enter password: "))
        user.save()
        print("SuperUser Created!")
    except Exception as exc:
        print(str(exc))
