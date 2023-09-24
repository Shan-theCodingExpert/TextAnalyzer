# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render # to use template file



def index(request):  # def is ude to define function  it takes argument 'request'
    return render(request, 'index.html')  # render used argument 1. request  2. id file name we want  i.e. index.html here


def analyze(request):  #analyze is also a function
    #Get the text
    djtext = request.POST.get('text', 'default')     # to get the text putted in text form at frontend

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')        # removepunc variable is storing the checkbox value, if checkbox is not marked it will store 2nd argument i.e. off
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover','off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''   # we stored al types of punctuation in punctuation variable
        analyzed = ""                                       # declared a string analyzed
        for char in djtext:                                 # iterating char in djtext
            if char not in punctuations:                    # checking if char not in punctuation
                analyzed = analyzed + char                  # then add it in analyzed

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}  #params is a dict which store something// we will use it in analyze.html.in template file
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                    if not(djtext[index] == " "):
                        analyzed = analyzed + char

            elif not(djtext[index] == " " and djtext[index+1]==" "):                        
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    
    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and numberremover != "on"):
        return HttpResponse("please select any operation and try again")  # HttpResponse is used to return as to return this we have no html file in template created so we can't use render

    return render(request, 'analyze.html', params)   # we are having analyze,html were we need this param dictionary so we used here render to acces html file in template

def about(request):
    return render(request, 'about.html')