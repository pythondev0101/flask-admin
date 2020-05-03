Command Line Manager
====================

Ito yung mga commands sa terminal na magagamit mo sa paggawa o paggamit ng system.
Kung naglalaravel ka ito yung mga 'php artisan make:controller' o kung ano ano pang framework jan na nagamit mo
sa school o sa trabaho.

Sa application framework na to may mga ilan din tayong ganyan mga commands na matatype mo sa terminal

Ito yung mga sumusunod:

- **help** - Para makita mo yung mga commands na pwedeng gamitin

- **install** - Mag iinsert ng mga initial na data sa database

- **create_superuser** - Mag crecreate ng superuser o owner o pinaka admin ng system

- **create_module** - Gagawa ng initial na folder at files ng module na gagawin mo

.. note:: Yang mga yan yung pwede mong itype sa terminal basta nasa project folder ka

Dito ituturo kung pano gamitin yang mga commands na yan

help
----

    Para magamit itype mo lang to sa terminal::

        $ flask core --help
    
    .. note:: 'flask' yung pinakaframework na ginamit at 'core' yun yung pinakamodule ng project na to, nandito yung mga commands kasi
    
Makikita mo na yung listahan ng mga commands

install
-------

    Basically, kailangan mo tong gawin sa pag installation, so nagawa mo na to dapat sa installation.
    Para magamit::

        $ flask core install

Sa ngayon makikita mo nag iinsert lang sya ng data sa database, tulad ng cities at provinces para hindi ka mag mano mano
mag insert ng mga yan, ginawa ko na yun para sayo, para di ka na mahirapan hehe

create_superuser
----------------

    Nagawa mo na din tong command na to sa installation palang, kasi di ka makakapaglogin ng walang user syempre

    Pero pwede pa din syang magamit kahit ilang beses, basically pwedeng maraming superuser sa system::

        $ flask core create_superuser

    .. note:: Enter mo yung first name,last name,username,email at password

Mag crecreate lang to ng superuser then may sasabihin na "Superuser created successfully!"

create_module
-------------

    Kung gagawa ka ng module mo, itype mo lang to::

        $ flask core create_module module_name

    .. note::Yung module_name palitan mo kung anong pangalan ng module mo

Mag crecreate to ng module folders(structure) at files at mga initial codes na kailangan mong palitan

Salamat sa pagbabasa, madami pa to hehe
---------------------------------------