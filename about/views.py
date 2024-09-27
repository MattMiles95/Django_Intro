from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def about_me(request):
    return HttpResponse("Hello from the 'about' app, World!")