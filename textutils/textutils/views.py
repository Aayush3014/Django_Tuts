# Created by me not default.
from django.http import HttpResponse
from django.shortcuts import render



def index(request):

    return render(request,'index.html')
    # return HttpResponse("<h1>Home</h1>")

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')


# def newlineremove(request):
#     return HttpResponse("new line remove")

# def charcount(request):
#     return HttpResponse("print character count")

# def spaceremove(request):
#     return HttpResponse("<h1>SpaceRemover page</h1>")

# def capitalizefirst(request):
#     return HttpResponse("<h1>space removal page</h2>")