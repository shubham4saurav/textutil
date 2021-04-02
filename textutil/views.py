from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'main.html')

def displaypage(request):
    
    text1 = request.GET.get('text','default')
    print(text1)
    removepunc =  request.GET.get('removepunc','off')
    fullcaps =  request.GET.get('fullcaps','off')
    
    extraspaceremover =  request.GET.get('extraspaceremover','off')

    if removepunc =='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ''
        for  char in text1:
            if char not in punctuations:
                analysed = analysed+char
        params = {'purpose':'removed punctuations ','words':analysed} 
        text1 = analysed       
    if fullcaps =='on':
        analysed = ''
        for char in text1:
            analysed+=char.upper()
        params = {'purpose':'Uppercase ','words':analysed}    
        text1 = analysed 

    if extraspaceremover=="on" :
        analysed = ""
        for index, char in enumerate(text1):
            if not(text1[index] == " " and text1[index+1]==" "):
                analysed = analysed + char

        params = {'purpose': 'Removed NewLines', 'words': analysed}
        text1 = analysed    

    
    return render(request,'displaypage.html',params)    


def about(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contact.html')