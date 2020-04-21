from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def predictOnLink(request):
    if request.method=='POST':
        string = str(request.POST.get('URL'))
        if string is not None:
            url = {'url': string,'show':True}
            return render(request,'index.html',url)
        else:
            return render(request,'index.html',{'show':False})
    return render(request, 'index.html',{'show':False})

def automatedTesting(request):
    return render(request,'automated_testing.html')