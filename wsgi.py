import os
from app import create_app
from dotenv import load_dotenv


load_dotenv()
config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()