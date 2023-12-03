from django.shortcuts import render

# Create your views here.

def respond(request):
    return render(request,'respond.html')

