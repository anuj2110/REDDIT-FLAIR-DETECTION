from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from .predictor import *
import os
from django.conf import settings
# Create your views here.
 

def predictOnLink(request):
    if request.method=='POST':
        url = str(request.POST.get('URL'))
        if url is not None:
            pred = makePredictions(url,ml_model,preprocessor,reddit,stopwords,labeltoflair)
            return render(request,'index.html',{'url':pred,'show':True})
        else:
            return render(request,'index.html',{'show':False})
    return render(request, 'index.html',{'show':False})
@csrf_exempt
def automatedTesting(request):
    if request.method=='POST':
        myfile = request.FILES['upload_file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        # myfile = open(os.path.join(settings.MEDIA_ROOT, filename), 'rb')
        url_dict={}
        with open(os.path.join(settings.MEDIA_ROOT, filename), 'r') as var:
            for url in var:
                url = url.rstrip()
                url_dict[url]= makePredictions(url,ml_model,preprocessor,reddit,stopwords,labeltoflair)
        os.remove(path=os.path.join(settings.MEDIA_ROOT, filename))
        return JsonResponse(url_dict)
    return render(request,'automated_testing.html')