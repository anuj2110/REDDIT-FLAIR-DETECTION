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
        if url!="" and 'https://www.reddit.com/r/india/comments/' in url and url!='https://www.reddit.com/r/india/comments/':
            pred = makePredictions(url,ml_model,preprocessor,reddit,stopwords,labeltoflair)
            return render(request,'index.html',{'url':url,'show':True,'pred':pred})
        else:
            return render(request,'index.html',{'show':False,'error':'please enter a valid url'})
    return render(request, 'index.html',{'show':False})
@csrf_exempt
def automatedTesting(request):
    if request.method=='POST':
        try:
            myfile = request.FILES['upload_file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url_dict={}
            with open(os.path.join(settings.MEDIA_ROOT, filename), 'r') as var:
                for url in var:
                    url = url.rstrip()
                    if url!="" and 'https://www.reddit.com/r/india/comments/' in url and url!='https://www.reddit.com/r/india/comments/':
                        url_dict[url]= makePredictions(url,ml_model,preprocessor,reddit,stopwords,labeltoflair)
                    else:
                        url_dict[url]= "not a valid url"
            os.remove(path=os.path.join(settings.MEDIA_ROOT, filename))
            return JsonResponse(url_dict)
        except:
            return render(request,'automated_testing.html',{'error':"Please add a file"})
        
    return render(request,'automated_testing.html')