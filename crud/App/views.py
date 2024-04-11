from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views import View

from django.views.generic import CreateView

from .models import Customer 

# Create your views here.

class App(View):
    customers = Customer.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'customerdetails' : customers,
    }
    def get(self, request):
        return HttpResponse(self.template.render(self.context, request))
    
# def app(request):
#     return HttpResponse("Hello")

class Regitration(CreateView):
    model = Customer
    fields = [ 'fullname', 'age','gender', 'email', 'number', 'address', 'state', 'city', 'pincode', 'image']
    success_url= '/'
    # template_name = 'registration.html'
    
