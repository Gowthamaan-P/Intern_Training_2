from django.urls import path
from . import views

urlpatterns = [
    path("usercheck", views.usercheck, name="usercheck"),
    path("devicereg", views.devicereg, name="devicereg"),
    path("patientcheck", views.patientcheck, name="patientcheck"),  
    path("patientreg", views.patientreg, name="patientreg"),  
    path("patients", views.patients, name="patients"),  
    path("mydevices", views.mydevices, name="mydevices"),  
    path("alldevices", views.alldevices, name="alldevices"), 

]
