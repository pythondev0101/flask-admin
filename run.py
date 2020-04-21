import os
from app import create_app,db
# import subprocess

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()


# # TODO: Check mysql if running, turn on if not.
# # TODO: CHECK os
# # TODO: CHECK path of mysql or if it installed in environment variable
# if __name__ == "__main__":
#     if HomeBestConfig.HOMEBEST_SERVER == "XAMPP":
#         print(subprocess.check_output("mysql -u root"))
#         print("OK!")
#         app.run(host='0.0.0.0',port=8080)
