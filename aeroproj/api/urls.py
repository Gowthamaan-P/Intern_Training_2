from django.urls import path
from . import views

urlpatterns = [
    path('retPatientsData/', views.retPatientsData),
    path('addpatients/',views.addPatients),
    path('adddevices/',views.addDevices),
    path('logdata/',views.logdata),
]