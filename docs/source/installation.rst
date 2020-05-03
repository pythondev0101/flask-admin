Installation
============

Sa ngayon hindi pa sya package kaya, ang installation lang ay idodownload lang o icloclone(kung alam mo mag git)
sa github yung buong files.

For Ubuntu/linux users
----------------------

- **Una, Iinstall ang mga python3 dependencies**
    
    Para mainstall icopy at paste lang ito sa iyung terminal, una sa lahat wag mo icocopy yung '$'::

        $ sudo apt-get install python3-dev python3-pip

- **Pangalawa, iinstall ang at upgrade ang setuptools(wag magtaka, di ko din alam tong mga tools na to haha)**

    Para magawa to copy/paste lang din sa terminal::

        $ pip3 install --upgrade pip setuptools

- **Pangatlo, pumunta sa home folder**

    Para makapunta dun ganito lang itype mo sa terminal::

        $ cd ~
    
    .. note:: 'cd' = change directory at '~' = home folder
    
- **Pang-apat, magcreate ng 'venvs' na folder sa home folder**

    Para makapagcreate copy/paste mo lang ulit to::

        $ mkdir venvs
    
    .. note:: 'mkdir' = make directory at 'venvs' yun yung pangalan ng folder

- **Panglima, magcreate ng virtual environment o venv,para lahat ng iinstall na software papasok dito**

    Para makapagcreate copy/paste mo lang ulit to::

        $ python3 -m venv venvs/homebest

    .. note:: Ibig sabihin nito gagawa ng 'homebest'(folder) na venv sa 'venvs' na folder

- **Pang anim, iactivate yung virtual environment, para lahat na ng iinstall papasok sa folder na venvs/homebest**

    Copy/paste mo lang to sa terminal::

        $ source ~/venvs/homebest/bin/activate
    
    .. note:: Kapag naactivate mo, makikita mo sa terminal, may nakalagay ng homebest sa unahan

- **Pangpito, i-download mo na o i clone kung alam mo mag git sa github**

    Kung may git na naka install na sa pc mo, itype mo lang to::

        $ git clone -b develop git@github.com:pythondev0101/homebest-framework.git

    .. note:: Ibig sabihin nyan idodownload mo yung buong folder ng develop branch(malalaman mo to github pag cheneck mo hehe)

- **Pangwalo, punta ka sa na download mong folder, 'homebest-framework' pangalan nun**

    Pag nadownload mo na o na clone, dapat nasa home mo nadownload, itype mo lang to::

        $ cd homebest-framework

    .. note:: Kung dinownload mo, nasa downloads folder yun kaya imove mo sa home folder para magawa mo yung nasa taas

- **Pangsiyam, hanapin mo yung .env na file then palitan mo yung mga values**

    Ichange mo lang yung mga database_user, database_name ...
    Depende sa database mo syempre

- **Pangsampu, iinstall mo yung requirements.txt na nakalagay sa project folder**

    Dapat nasa project folder ka, tapos type mo to::

        $ pip3 install -r requirements.txt
    
    .. note:: Sana walang error hahaha, hintayin mo lang sana matapos na haha

- **Pang eleven(haha), run mo na yung project**

    Para marun, sa development server muna, type mo lang to::

        $ flask run
    
    .. note:: Tapos check mo sa browser, http://127.0.0.1:5000, pag walang error swerte mo haha

- **Pang twelve, mag create ka na ng superuser**

    Type mo lang to sa terminal::

        $ flask core create_superuser

    .. note:: Tapos sagutan mo lang yung mga tanong

- **Pang thirteen, last muna siguro to haha, type mo to**

    Type mo to para ma initialize yung mga data na kailangan ng system

        $ flask core install


Congrats, natapos mo!!! Isa kang alamat!!!
------------------------------------------

Marami ka pang babasahin,this is just the beningging...