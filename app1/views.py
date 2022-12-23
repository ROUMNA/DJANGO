from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import loader
from .models import user, formation as f

def python_profil(request) :
    template = loader.get_template("index_python.html")  
    return HttpResponse(template.render(request= request))

def data_science(request) :
    template = loader.get_template("index_ds.html")  
    return HttpResponse(template.render(request= request)) 

def trainer_profil(request) :
    template = loader.get_template("index_trainer.html")  
    return HttpResponse(template.render(request= request))
           

def page_acceuil(request) :
    template = loader.get_template("index_app.html")  
    return HttpResponse(template.render(request= request))    

def model_view (request):
    users = f.objects.filter()
    users_list = ["<li>{}   {} </li>".format(user.modul, user.prix) for user in users]
    message = """<ul>{}</ul>""".format("\n".join(users_list))
    return HttpResponse(message)

def index_app (request) :
    return HttpResponse("<h3>bonjour, je viens faire ma première application avec django. Merci</h3>")

def page_app(request):

    myDate = datetime.now()
    
    formatedDate = myDate.strftime("%d-%m-%y %H:%M:%S")

    # Do something with the formatted date
    return render(request, 'page.html', {'date': formatedDate})