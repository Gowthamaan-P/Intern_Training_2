from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import devicedata, patientdata, usermapping
from aerouser.models import userdata
#from aerodevice.views import login
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.core.mail import send_mail
import uuid, time, pyotp
from django.contrib import messages
from aerouser.views import gen_uid
import requests


def devicereg(request):

    #email_data = request.session.get('email')
    error_message = None 
    
    if request.method == 'POST':

        d_name = request.POST.get('device_name')
        serial_data = request.POST.get('serial_number')  
        model_data = request.POST.get('model')
        location_data = request.POST.get('location')
        status_data = "Idle"

        url = "http://127.0.0.1:8000/adddevices/"

        data = {
            'device_name' : d_name, 
            'model' : model_data, 
            'serial_number' : serial_data,
            'status' : status_data,
            'location' : location_data
        }

        print("Request Data:", data)

        response = requests.post(url, json=data)

        print(response.status_code)


        return redirect("login")
        
    else:
        return render(request, "devicereg.html",) 


def patientreg(request):
    email_data = request.session.get('doctor_email')
    error_message = None 
    patient_id = gen_uid()

    if request.method == 'POST':

        patientid_data = request.POST.get('patientid')
        patient_name_data = request.POST.get('patient_name')
        patient_age_data = request.POST.get('patient_age')
        patient_gender_data = request.POST.get('patient_gender')
        contact_data = request.POST.get('contact')
        emergency_data = request.POST.get('emergency')


        url = "http://127.0.0.1:8000/addpatients/"

        data = {
        'doctorid': email_data,
        'patientid': patientid_data,
        'patient_name': patient_name_data,
        'patient_age': patient_age_data,
        'patient_gender': patient_gender_data,
        'contact': contact_data,
        'emergency': emergency_data,
        }

        print("Request Data:", data)

        response = requests.post(url, json=data)

        print(response.status_code)
        print(response.json())
        context = request.session.get('context')
        return render(request,"landing.html", context)
        
    else:
        return render(request, "patientreg.html", {'email': email_data, 'patient_id':patient_id}) 


def mylog(request):
    email_data = request.session.get('doctor_email')
    sno_data = request.session.get('devicelog')

    devices_data = devicedata.objects.values()
    user_data = usermapping.objects.values()

    usertype = request.session.get('usertype')
    print(usertype)
    if usertype == "Superuser":
        temp = usermapping.objects.all().values()
        print("super user logged in")
    else:
        current_user_id = userdata.objects.filter(email=email_data).values()
        temp = usermapping.objects.filter(user=current_user_id[0]['id']).values()

    mes = []
    #print(current_user_id[0]["id"])
    for i in temp:
        mes.append(i)
    #print(mes)
    context = {
        'messages': mes[::-1],
        'doctor_email': email_data,
        'device_name': sno_data,
        'usertype': usertype,
    }
    
    return render(request, "mylog.html",context)

def patients(request):
    email_data = request.session.get('doctor_email')
    usertype = request.session.get('usertype')

    print(usertype)
    if usertype != "Superuser":
        objects = patientdata.objects.filter(doctorid=email_data).values()
    else:
        objects = patientdata.objects.values()
    mes = []
    for i in objects:
        mes.append(i)
    #print(mes)
    context = {
        'messages': mes,
        'doctor_email': email_data,
        'usertype': usertype,
    }

    return render(request, "patients.html", context)


def alldevices(request):
    email_data = request.session.get('doctor_email')
    usertype = request.session.get('usertype')
    mes = []
    assign_status = "Assign Me"
    devices_data = devicedata.objects.values()
    for i in devices_data:
        if i['assignuser_id'] != None:
            temp = userdata.objects.filter(id=i['assignuser_id']).values()
            assign_status = [j['email'] for j in temp]
            i['assign_status'] = assign_status[0]
        mes.append(i)

    #print(mes)

    context = {
        'messages': mes,
        'doctor_email': email_data,
        'usertype': usertype,
    }

    return render(request, "alldevices.html", context)
