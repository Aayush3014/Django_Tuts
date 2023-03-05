# Created by me not default.
from django.http import HttpResponse

def index(request):
    # Adding a website link
    return HttpResponse('''<h1>Hello ayush this is the first page.</h2> <a href = https://github.com/Aayush3014/Django_Tuts>Ayush Github <a/>''')

def about(request):
    return HttpResponse("This is the about page.")