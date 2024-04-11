from django.urls import path

from . import views


urlpatterns = [
    path('', views.App.as_view(), name='app'),
    path('registration',views.Regitration.as_view(), name='registration'),
    # path('app', views.app, name='app'),
]