from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Entry
from django.db import IntegrityError
def home(request):
    return render(request,"home.html")

def show(request):
    data= Entry.objects.all()
    return render(request,"show.html",{'data': data})

def send(request):
    if request.method =="POST":
        ID = request.POST['id']
        NAME = request.POST['name']
        EMAIL = request.POST['email']
        try:
            if(ID and NAME and EMAIL): # can't store null details in the table
                entry_id=Entry.objects.get(ID=ID) #can't store same id
                msg="Id already exists" 
                return render(request, "home.html",{"msg":msg })
            else:
                msg="Fill all the Details"
                return render(request, "home.html",{"msg":msg })
        except:
            try:
                entry_with_email = Entry.objects.get(EMAIL=EMAIL) #email should be unique -- error handeling
                msg="Email already exists."
                return render(request, "home.html",{"msg":msg })
            except Entry.DoesNotExist:
                Entry(ID=ID, NAME=NAME, EMAIL=EMAIL).save()   #unique email
                msg="Data stored succesfully"
                return render(request, "home.html",{"msg":msg })
    else:
        return HttpResponse("<h1>404- Not found</h1>")

def delete(request):
    ID= request.GET['id']
    Entry.objects.filter(ID=ID).delete()
    return HttpResponseRedirect("show")

def edit(request):
    ID=request.GET['id']
    NAME=EMAIL="NA"
    for data in Entry.objects.filter(ID=ID):
        NAME= data.NAME
        EMAIL=data.EMAIL
    return render(request,"edit.html",{'ID':ID,'NAME':NAME,'EMAIL':EMAIL})

def RecordEdited(request):
    if request.method=="POST":
        ID=request.POST['id']
        NAME=request.POST['name']
        EMAIL=request.POST['email']
        Entry.objects.filter(ID=ID).update(NAME=NAME, EMAIL=EMAIL)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found </h1>")
