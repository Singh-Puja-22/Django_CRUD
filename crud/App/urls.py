from django.urls import path

from . import views


urlpatterns = [
    path('', views.App.as_view(), name='app'),
    path('registration',views.Regitration.as_view(), name='registration'),
    path('customer',views.CustomerList.as_view(), name='customer'),
    path('editcustomer/<int:pk>', views.UpdateCustomer.as_view(), name='editcustomer'),
    # path('app', views.app, name='app'),
]