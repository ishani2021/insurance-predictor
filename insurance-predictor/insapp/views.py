from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is the home page.")


def about(request):
    return HttpResponse("About page.")