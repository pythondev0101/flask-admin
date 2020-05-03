Create a Module - Part 3
========================

Nagawa na natin iinclude ang module natin, ngayon mag eedit nalang tayo, code nalang code.
Dito sa part na to magagamit na natin yung mga functions ng **admin** module like **admin_index**. 
Itong **admin_index** na to pag ginamit mo to sa route mo sample sa pagpapakita ng list ng cars, 
hindi mo na kailangan mag create ng html o mag code ng pagkahaba haba para mapakita lang sa browser.

**admin_index** na function mag aaccept lang sya ng mga data then ayun may 'list of cars' page ka na.

Ang gagawin natin ngayon ay page na pinapakita ang list ng cars, naka html table ito.

So para mas maintindihan mo, sundan mo lang tong steps ulit hehe:

Una, Imomodify natin ang routes.py, iupdate natin yung route na '/cars'
-----------------------------------------------------------------------

    1.1. Iimport muna ang 'admin_index' at Car model sa taas ng routes.py ng module mo::

        .. code-block:: python

            # Ito yung pag import
            from app.admin.routes import admin_index
            from .models import Car

            # existing code ...
            @bp_test_module.route("/cars")
            def cars():
                # Sa ngayon text lang muna ipakita natin
                return "Cars1,Cars2"

    1.2. Gumawa ng list na 'fields' sa loob ng function::

        .. code-block:: python

            # existing import code

            # Change na natin 
            @bp_test_module.route("/cars")
            def cars():
                # Ito yung fields
                # Ilagay ang mga columns na gusto mong ipakita sa table list
                # Mandatary ang paglagay ng id sa unahan ng fields
                fields = [Car.id,Car.name,Car.color]
                
                # existing code
        
Pangalawa, Gumawa ng form na CarForm
------------------------------------

    .. note:: Kailangan ng form kasi need ng admin_index yun as v1.4

    2.1. Mag create ng file na 'forms.py' kasama ng mga models.py at routes.py::

        | app
        | ├── test_module
        | │   ├── __init__.py
        | │   ├── test_module.py
        | │   ├── models.py
        | │   ├── routes.py
        | |   └── forms.py
        | ├── admin
        | ├── auth
        | ├── core
        | └── __init__.py

    2.2. Iopen at iimport ang mga kailangan gamitin::

        .. code-block:: python

            # imports
            # AdminIndexForm at AdminCreateField ay kailangan sa paggamit ng admin_index
            from app.admin.forms import AdminIndexForm, AdminCreateField
            # Flask imports na tong mga to
            from wtforms.validators import DataRequired
            from wtforms import StringField, IntegerField

    2.3. Gumawa ng class gamit ang AdminIndexForm::

        .. code-block:: python

            class CarForm(AdminIndexForm):

                # Ito yung mga data na kailangan natin, gayahin lang to
                name = StringField(validators=[DataRequired()])
                color = StringField(validators=[DataRequired()])

                # Gumawa ng mga AdminCreateFields, ito yung magpapakita sa form na inputs

                a_name = AdminCreateField('name', 'NAME', 'text')
                a_color = AdminCreateField('color', 'COLOR', 'text')

                # 'name' = name at id ng html input
                # 'NAME' = label ng html input
                # 'text' = type ng html input

                # Iimplement ang create_fields ng AdminIndexForm
                create_fields = [
                    [a_name,a_color]
                ]

                # Iimplement ang mga sumusunod ng AdminIndexForm
                
                # Header ng html table(ito yung makikita sa taas ng columns ng table sa page)
                index_headers = ['Name', 'Color']

                # Ito yung title ng page
                index_title = "Cars"
                
                # Optional lang tong message na to
                index_message = "List of Cars"

    2.4. Saved!

Pangatlo, Bumalik sa routes.py sa function na cars() at imodify
---------------------------------------------------------------

    3.1. Iimport ang CarForm() na ginawa natin sa routes.py::

        .. code-block:: python

            # existing import code

            # Ito copy paste mo 
            from .forms import CarForm

            # existing code

    3.2. Imodify yung function na cars() at iinstance yung CarForm()::

        .. code-block:: python

            # existing import code

            # Change na natin ulit
            @bp_test_module.route("/cars")
            def cars():
                # Ito yung fields
                # Ilagay ang mga columns na gusto mong ipakita sa table list
                # Mandatary ang paglagay ng id sa unahan ng fields
                fields = [Car.id,Car.name,Car.color]
                
                # ito yung pag iinstance
                form = CarForm()

                # existing code...

    3.3. Ireturn ang admin_index sa function na cars()::

        .. code-block:: python

            # existing import code

            # Change na natin ulit
            @bp_test_module.route("/cars")
            def cars():
                # Ito yung fields
                # Ilagay ang mga columns na gusto mong ipakita sa table list
                # Mandatary ang paglagay ng id sa unahan ng fields
                fields = [Car.id,Car.name,Car.color]
                
                # ito yung pag iinstance
                form = CarForm()

                # Ito yung pag return kasama ng mga ginawa nating variables
                # False muna natin yung ibang parameters kasi hindi pa natin na implement
                
                return admin_index(Car,fields=fields,form=form,url='bp_test_module.cars',create_modal=False, \
                    view_modal=False)

    3.4. Saved!

        .. note:: url = yun yung route ng function na to kaya ('bp_test_module.cars')

        .. note:: False yung create_modal at view_modal kasi di pa natin na implement yung mga create at edit function ng car

Pang-apat, Check ang browser
----------------------------

    4.1.  Sa may navbar click mo yung Cars>View Cars.

    4.2. Surprise meron ka ng html page agad nang ganun lang hehe

No html codes, pure python nalang ang gagawin mo sa pag render ng mga data sa browser.

Listahan palang yan, sa susunod na tutorial kung pano naman magkakaroon ng create forms at edit forms na python lang icocode 
hindi muna kailangan mag html.

Thanks sa pagbasa...