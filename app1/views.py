from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def app1(request):
    return HttpResponse("Hello world test!")

def app2(request):
    return HttpResponse("Hello world test app2!")





