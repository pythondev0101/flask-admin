""" THIS FILE IS FOR INITIAL SETUPS """
import pymysql.cursors
import argparse
from config import HomeBestConfig as config
from werkzeug.security import generate_password_hash
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("create_superuser", help="Create a System SuperUser")
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

    # TODO: Create ng command para iinstall o isetup mga urls at templates ng module
    """
    if args.install -module 
    """