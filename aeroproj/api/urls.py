from django.urls import path
from . import views

urlpatterns = [
    #path('', views.getData),
    path('addpatients/',views.addPatients),
    path('adddevices/',views.addDevices),
]