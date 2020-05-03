Create a Module
===============

Ang application framework na to ay nabubuo ng mga tinatawag na modules, ang mga built-in modules ay 
ang **core**, **auth** at **admin**. Itong tatlo na to makikita nyo folder nila sa app/ folder. Basically
itong tatlo ay **blueprints** ng Flask, kapag alam nyo na ang Flask o may kunting nalalaman, hindi kayo mahihirapan sa Paggawa
dahil pinadali na ng project na yung paggawa ng mga modules. 

Ang paggawa ng module, ay parehas sa paggawa ng blueprint sa Flask. Ang pinagkaiba lang sa project na to 
ay kung papaano mo iinclude yung module mo sa **admin** module. Yung **admin** module kasi sya yung nakikita mo sa website.
So kung gusto mo iinclude at talagang iinclude mo sya sa admin kasi kung hindi walang gui ang module mo hehe.

Sundan lang natin ang mga sumusunod na steps para di malito sa mga nangyayari...

Una, gamitin ang command na create_module sa yung terminal
----------------------------------------------------------

    Copy/paste ang mga sumusunod, wag isama yung '$'::

        $ flask core create_module test_module

    .. note:: Dapat nasa loob ka ng project at virtual environment, palitan mo yung 'test_module' sa module mo

    Makikita mo na sa app/ folder yung module na nacreate, icheck mo na yung mga files
    Ito yung magiging structure::

        | app
        | ├── test_module
        | │   ├── __init__.py
        | │   ├── test_module.py
        | │   ├── models.py
        | │   └── routes.py
        | ├── admin
        | ├── auth
        | ├── core
        | └── __init__.py

    .. note:: 'test_module' kunwari yung module na ginawa mo

    So nagcreate sya ng folder na 'test_module' at mga files na **__init__.py**, **test_module.py**
    **models.py**, **routes.py** at mamaya ng yung **templates** na folder

Pangalawa,Palitan ang mga nakalagay na code sa mga files na nacreate, sundan mo to
----------------------------------------------------------------------------------

    - **__init__.py** - dyan mo iinitialize yung blueprint ng flask

    .. code-block:: python

        from flask import Blueprint # Import yung blueprint

        # Mag iinitialize ng blueprint na variable para ma include ito mamaya
        bp_test_module = Blueprint('bp_test_module', __name__,)
        
        # Import ang lahat ng laman ng routes.py at models.py
        from . import routes
        from . import models

    - **models.py** - Parang ito yung mga tables ng module mo. Dito mo gagawin

    .. code-block:: python

        # Import yung db ng app
        # from app import db

        # Gawa ng class model, gagawa ito ng table sa database
        class Car(db.Model):
            # lagyan ng table
            __tablename__ = "tbl_cars"

            # Lagyan ng primary column
            id = db.Column(db.Integer, primary_key=True)

            # Lagyan ng mga column
            name = db.Column(db.String(64), nullable=False)
            color = db.Column(db.String(64), nullable=False)

            # ito yung mga makikita mo sa admin page sa may navigation bar
            model_name = 'Cars'
            model_icon = 'pe-7s-cars'
            model_description = "CARS"

            # ito yung mga link sa baba ng navigation bar pa clinick mo
            functions = {'View Cars': 'bp_test_module.cars'}


    - **routes.py** - Dito mo ilalagay yung mga routes(sample. myproject.com/cars = List ng cars makikita sa browser)
    
    .. code-block:: python

        # Import ang ginawa nating blueprint
        from app.test_module import bp_test_module

        # Gumawa ng route

        @bp_test_module.route("/cars")
        def cars():
        # Sa ngayon text lang muna ipakita natin
            return "Cars1,Cars2"
        
    .. note:: Hindi nyo muna makikita yung mga ginawa natin kasi hindi pa natin na iinclude ito sa system

Pangatlo, iinclude na sa system ang iyong module
------------------------------------------------

    Pag na include na sa system ang iyong module, maisasama na yung mga models(tables) sa pagcrecreate ng tables 
    at routes(links) para pwede mo ng makita sa browser yung mga text o page mo.

    Sundan ang mga sumusunod na step:

        3.1. Open mo yung __init__.py sa app/ folder hindi yung nasa module mo

        3.2. Hanapin yung create_app na function, sa loob nito may app_context(), punta ka dun

            .. code-block:: python

                def create_app(config_name):
                
                # ...

                with app.app_context():
                
                # Dito ka mag momodify

        3.3. Iimport sa may SYSTEM MODULES yung module mo, ganito

            .. code-block:: python

                """EDITABLE: IMPORT HERE THE SYSTEM MODULES  """
                from app.core import bp_core
                from app.auth import bp_auth
                from app.admin import bp_admin

                # Dito mo iimport sa baba

                from app.test_module import bp_test_module

                # Inimport natin yung ginawa natin kaninang variable sa may __init__.py ng module
                
                """--------------END--------------"""
        
        3.4. Pagkatapos nun, Ireregister na natin yung Inimport nating module sa may MODULE BLUEPRINTS

            .. code-block:: python

                """EDITABLE: REGISTER HERE THE MODULE BLUEPRINTS"""
                app.register_blueprint(bp_core, url_prefix='/')
                app.register_blueprint(bp_auth, url_prefix='/auth')
                app.register_blueprint(bp_admin, url_prefix='/admin')

                # Dito mo Iregister sa baba

                app.register_blueprint(bp_test_module, url_prefix='/test_module)

                # Yan yung pang register, tapos nilagyan natin ng 'url_prefix=/test_module' para lahat ng
                # routes o links ng module mo magsisimula sa '/test_module/' (example. myproject.com/test_module/cars)
                
                """--------------END--------------"""

        3.5. Tapos pagka 'flask run' mo ulit, madedetect na ng system yung mga tables na ginawa mo kaya icrecreate nya na at links

            $ flask run

        .. note:: 
            Check mo yung browser, then type mo sa url address 127.0.0.1:5000://test_module/cars, makikita mo na yung ginawa mong route
            Check mo din yung database mo makikita mo na yung tbl_cars dun

So yan palang yung basics ng pagcreate ng module o blueprint, sa susunod na tutorial iinclude naman natin yung module natin sa admin module
para iinherit o makapag create kayo ng mga page ng hindi na kayo gagawa ng html.

Basta basa lang ng basa hehe...

