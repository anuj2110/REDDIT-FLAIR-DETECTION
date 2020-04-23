from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .predictor import *
# Create your views here.


def predictOnLink(request):
    if request.method=='POST':
        string = str(request.POST.get('URL'))
        if string is not None:
            pred = makePredictions(string,ml_model,preprocessor,reddit,stopwords,labeltoflair)
            return render(request,'index.html',{'url':pred,'show':True})
        else:
            return render(request,'index.html',{'show':False})
    return render(request, 'index.html',{'show':False})

def automatedTesting(request):
    if request.method=='POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

    return render(request,'automated_testing.html')