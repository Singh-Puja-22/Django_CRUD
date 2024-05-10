from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View


from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

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

class Regitration(CreateView):
    model = Customer
    fields = [ 'fullname', 'age','gender', 'email', 'number', 'address', 'state', 'city', 'pincode', 'image']
    success_url= '/'

class CustomerDetail(DetailView):
    queryset = Customer.objects.all()
    template_name = 'customer_detail.html'

class CustomerList(ListView):
    queryset = Customer.objects.all()
    template_name = 'customer.html'

class UpdateCustomer(UpdateView):
    model = Customer
    fields = [ 'fullname', 'age','gender', 'email', 'number', 'address', 'state', 'city', 'pincode', 'image']
    success_url = '/customer'
    # success_url= '/customerdetail/customer.pk'
    # success_url=reverse_lazy("App:customerdetail")

class DeleteCustomer(DeleteView):
    model = Customer
    template_name = 'customer_delete.html'
    success_url = '/customer'
    
