from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index_template_app(request) :
    return render(request, "business-2/business-2/index.html")

def index_app (request) :
    return HttpResponse("<h3>bonjour, je viens faire ma première application avec django. Merci</h3>")


def page_app(request):

    myDate = datetime.now()
    
    formatedDate = myDate.strftime("%d-%m-%y %H:%M:%S")

    # Do something with the formatted date
    return render(request, 'page.html', {'date': formatedDate})