from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def predictOnLink(request):
    return render(request, 'index.html')

def automatedTesting(request):
    return render(request,'automated_testing.html')