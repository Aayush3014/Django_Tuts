# Created by me not default.
from django.http import HttpResponse
from django.shortcuts import render



def index(request):

    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text','default')

    # Check values for checkbox.
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    spaceremover = request.GET.get('spaceremover','off')

    # if removepunc checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    # if fullcaps checkbox is on
    elif (fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    # if newlineremover is on
    elif (newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char
        params = {'purpose': 'New Lines Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    # If Space remover is on.
    elif (spaceremover=='on'):
        analyzed = ""
        for char in djtext:
            if char!=' ':
                analyzed = analyzed + char
        params = {'purpose': 'Spaces Removed', 'analyzed_text': analyzed}
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