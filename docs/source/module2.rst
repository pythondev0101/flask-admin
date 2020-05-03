Create a Module - Part 2
========================

Ito yung continuation ng Create a Module, sa unang part na include na natin yung module natin sa system,
ang mangyayari dun yung madedetect yung mga tables then iccreate ng system tapos madedetect na din yung mga routes o 
links para mapakita sa browser.
Sa part naman na to, iinclude natin sa **admin** module yung module natin. Ang mangyayari dito pag na include na natin, 
automatic gagawa ang **admin** module ng mga html pages tapos irerender nya o ipapakita nya sa **admin page**.

Gawin natin to para mas maintindihan mo, sundan mo lang mga steps na to:

Una, mag create ng python file sa loob ng iyong test_module na folder
---------------------------------------------------------------------

    1.1. Mag create ng python file na ang pangalan 'test_module.py' o kung anong pangalan ng module mo

    1.2. Kapag nakapag create ganito ang folder structure na mangyayari::

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

Pangalawa, open at modify ang test_module.py
--------------------------------------------

    2.1. Gumawa ng class o Copy paste at basahin ng mabuti ang susunod na lines ng code

        .. code-block:: python

            # Iimport mo yung Car Model na ginawa natin sa models.py para mainclude sa admin page
            from .models import Car

            # Ito yung class na iimport natin mamaya kahit anong name nya, pero mas okay na pangalanan mo syang ng ganito
            # 'Test' name ng module mo + 'Module' sa dulo. 
            # Parang ganito:

            class TestModule():

                # name ng module 
                module_name = 'test_module'

                # icon ng module na makikita mo sa admin page(fa-home muna pero marami pang pwedeng pagpilian)
                module_icon = 'fa-home'

                # Ito yung link pag clinick mo yung icon dun pupunta
                # sample yung 'cars' na ginawa natin sa routes.py
                module_link = 'bp_test_module.cars'

                # Yung text na makikita sa tabi ng icon
                module_description = 'Administrator'

                # Dito mo ilalagay kung ano yung mga models na iinclude mo sa admin page
                # Car yung inimport natin sa taas
                models = [Car]

    2.2. Saved ang test_module.py

Pangatlo, Iinclude na sa app/__init__.py ang ginawa nating class
----------------------------------------------------------------

    3.1. Open mo yung __init__.py sa app folder hindi ung nasa module mo

    3.2. Punta ka ulit sa app_context() at sa loob hanapin mo yung comment na ``"""EDITABLE: INCLUDE HERE YOUR MODULE Admin models FOR ADMIN TEMPLATE"""``

    3.3. Import mo yung module dun:

        .. code-block:: python

            """EDITABLE: INCLUDE HERE YOUR MODULE Admin models FOR ADMIN TEMPLATE"""
            from app.admin.admin import AdminModule

            # Dito mo iimport 
            from app.test_module.test_module import TestModule

            # Then iadd mo sa modules na list
            modules = [AdminModule, TestModule]

            """--------------END--------------"""

    3.4. Saved and run, Check mo ung admin page kung nandun na yung module mo

    .. note:: Yung icon at description palang makikita mo at pagclinick mo yun, makikita mo na yung cars na page

