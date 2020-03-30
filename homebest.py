""" THIS FILE IS FOR INITIAL SETUPS """
import pymysql.cursors
import argparse
from config import HomeBestConfig as config
from config import basedir
from werkzeug.security import generate_password_hash
import os
from shutil import copyfile


def create_superuser(fname,lname,username,password):
    connection = pymysql.connect(host=config.HOMEBEST_HOST,
                                 user=config.HOMEBEST_USER,
                                 password=config.HOMEBEST_PASSWORD,
                                 db=config.HOMEBEST_DATABASE,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `auth_user` (`username`, `fname`,`lname`,`password_hash`,`image_path`,`active`,`email`) VALUES (%s, %s,%s, %s,%s,1,'')"
            image_path = 'img/user_default_image.png'
            cursor.execute(sql, (username, fname,lname,generate_password_hash(password),image_path))
        connection.commit()
    finally:
        connection.close()
    return True

def create_module(module_name):
    try:
        # TODO: FOR FUTURE VERSION CHECK OS
        module_path = basedir + "\\app" + "\\" + module_name
        templates_path = basedir + "\\app" + "\\templates" + "\\" + module_name
        core_init_path = basedir + "\\app" + "\\core" + "\\module_template" + "\\__init__.py"
        core_models_path = basedir + "\\app" + "\\core" + "\\module_template" + "\\models.py"
        core_routes_path = basedir + "\\app" + "\\core" + "\\module_template" + "\\routes.py"
        core_file_list = [core_init_path,core_models_path,core_routes_path]
        if not os.path.exists(module_path):
            os.mkdir(module_path)
            os.mkdir(templates_path)
            for file_path in core_file_list:
                file_name = os.path.basename(file_path)
                copyfile(file_path, os.path.join(module_path,file_name))

    except OSError:
        print("Creation of the directory %s failed" % module_path)
    else:
        print("Successfully created the directory %s " % module_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--create_superuser",help="Create a System SuperUser",action='store_true')
    parser.add_argument("--create_module", help="Create a System Module",type=str)
    args = parser.parse_args()

    # TODO: kung create na ang superuser dapat magproprompt na, na create na
    if args.create_superuser:
        fname = input("Enter First name:")
        lname = input("Enter Last name:")
        username = input("Enter Username:")
        password = input("Enter Password:")

        if create_superuser(fname, lname, username, password):
            print("SuperUser created!")
        else:
            print("SuperUser not created!")
    elif args.create_module:
        create_module(args.create_module)
