# Created by me not default.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello ayush this is the first page.")

def about(request):
    return HttpResponse("This is the about page.")