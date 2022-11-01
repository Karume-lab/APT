#Contains functions and classes that deal with requests and responds to the user requests

from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')

def contact(request):
    name= request.GET.get("name")
    message= request.GET.get("message")
    print(name, message)
    if request.method == "POST":
        name= request.POST.get("name")
        message= request.POST.get("message")
        print(name, message)
    return render(request, "contact.html")
# Create your views here.


