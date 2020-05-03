Maligayang pagdating sa HomeBest-Framework's documentation!
===========================================================

Ang project na ito ay para sa mga gustong gumawa ng system 
(eg. Project management system, Billing system, Fixed asset management system, Food ordering system,
POS, etc...) kung ano ano pang mga system na kadalasan pinapagawa sa school like thesis o simpleng school project
o kaya mga system na ginagamit talaga sa industry. 

Ang main goal kasi ng project na to eh lahat ng nabanggit sa taas, e mapapadali nalang ng application framework na ito,
hindi nyo na uulitin gumawa ng login/logouts nanaman kada project o kaya gagawa nanaman kayo ng mga tables tulad ng tbl_users, tbl_customers
blah blah blah... nakakaumay kasi talaga yung ganun. Sa application framework na to, hindi na kayo magsstart sa umpisa kasi ready to use na sya.
Ibig sabihin mo pwede mo na syang gamitin like pwede ka ng mag login, create ng users, may admin dashboard na din agad na magagamit mo.
Basically system na sya, tong application framework na to parang (laravel-admin,django-admin,flask-admin) na may created functionalities na

Ang gagawin mo nalang ay basahin tong documentation ng maayos, tapos tada basic system na!
Dahil nag create na kami ng mga functions para sayo na tatawagin mo na lang tapos meron na syang mapapakita sa browser

Gawa sya sa Flask, so kailangan mo matutunan kunti yung Flask (kahit kunti lang hehe)

Sample ganito:

.. code-block:: python

  @app.route("/customers")
  def list_of_customers()): 
    # Gusto mong ipakita yung list ng customers sa website mo
    # kunwari ito yung function o route na magrerender sa website
    # (pag di maintindihan, aralin mo lang kunti yung Flask hehe) 

    model = Customer
    fields = [Customer.id,Customer.fname,Customer.phone]
    return admin_index(model,fields)
    # admin_index() - isa yan sa functions na tinutukoy kanina na magpapadali ng buhay mo hehe

Tada!!! may webpage ka na nagpapakita ng list of customers na ganun ganun lang, basic diba?

Yan yung goal na sinasabi ko, madami pang pwedeng gawin sa application framework na to hindi lang yan, kaya magbasa ka pa! Hehehe

                            
   

