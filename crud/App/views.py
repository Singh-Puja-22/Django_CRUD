from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

class App(View):
    def get(self, request):
        return HttpResponse("Hello all!")
    
def app(request):
    return HttpResponse("Hello")
