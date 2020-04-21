from django.urls import path,include
from .views import *


urlpatterns = [
    path('',predictOnLink),
    path('automated_testing',automatedTesting)
]