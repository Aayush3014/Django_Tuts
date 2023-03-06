# Created by me not default.
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    parameter = {"name":"Ayush","Place":"Delhi"}
    return render(request,'index.html',parameter)
    # return HttpResponse("<h1>Home</h1>")

def removepunctuation(request):
    return HttpResponse("remove punctuation")

def newlineremove(request):
    return HttpResponse("new line remove")

def charcount(request):
    return HttpResponse("print character count")

def spaceremove(request):
    return HttpResponse("<h1>SpaceRemover page</h1>")

def capitalizefirst(request):
    return HttpResponse("<h1>space removal page</h2>")