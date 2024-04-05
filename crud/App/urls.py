from django.urls import path

from . import views


urlpatterns = [
    path('', views.App.as_view(), name='app'),
    path('app', views.app, name='app'),
]