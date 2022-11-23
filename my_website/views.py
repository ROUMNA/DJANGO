from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index_template(request) :
    return render(request, "index.html")

def index (request) :
    return HttpResponse("<h3>bonjour, je viens faire ma première vue avec django. Merci</h3>")

def page(request):

    myDate = datetime.now()
    
    formatedDate = myDate.strftime("%d-%m-%y %H:%M:%S")

    # Do something with the formatted date
    return render(request, 'page.html', {'date': formatedDate})