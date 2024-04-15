from django.urls import path

from . import views


urlpatterns = [
    path('', views.App.as_view(), name='app'),
    path('registration',views.Regitration.as_view(), name='registration'),
    path('customer',views.CustomerList.as_view(), name='customer'),
    path('customerdetail/<int:pk>',views.CustomerDetail.as_view(), name='customerdetail'),
    path('editcustomer/<int:pk>', views.UpdateCustomer.as_view(), name='editcustomer'),
    path('deletecustomer/<int:pk>', views.DeleteCustomer.as_view(), name='deletecustomer'),
    # path('app', views.app, name='app'),
]