from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.
def home(request):
    return render(request,"home.html",{})

def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request):
    return HttpResponse("<h1>Detail</h1>")

#Post data (context) from database to list.html (web page) 
def post_list(request):
    if request.user.is_authenticated():
        queryset = Question.objects.all()
        context = {
            "object_list": queryset,
            }
        return render(request,"list.html",context)
    else:
        return render(request,"home.html",{})
        
    

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
	
def androidapp(request):
    q = Question.objects.all()
    c = {
        "object_list": q,
    }
    return render(request,"HelloAndroid/www/index.html",c)
