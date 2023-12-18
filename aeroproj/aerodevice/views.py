from django.shortcuts import render, redirect, get_object_or_404
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
import requests, random
from django.utils import timezone

def rand_mac():
    hex = [random.choice('0123456789ABCDEF') for _ in range(12)]
    mac = ':'.join([''.join(hex[i:i+2]) for i in range(0, 12, 2)])
    return mac

def rand_model():
    m = [random.choice('0123456789GHIJKLMNOPQRABCDEFSTUVWXYZ') for _ in range(6)]
    model = ''.join([i for i in m])
    return model

def devicereg(request):

    #email_data = request.session.get('email')
    error_message = None
    mac = rand_mac()
    model_no = rand_model()
    if request.method == 'POST':

        d_name = request.POST.get('device_name')
        model_data = request.POST.get('model')
        serial_data = request.POST.get('serial_number')  
        lot_number = request.POST.get('lot_number')
        mfd_date = request.POST.get('mfd_date')
        battery_no = request.POST.get('battery_no')
        location_data = request.POST.get('location')
        status_data = "Idle"
        

        url = "http://127.0.0.1:8000/adddevices/"

        data = {
            'device_name' : d_name, 
            'model' : model_data, 
            'serial_number' : serial_data,
            'status' : status_data,
            'location' : location_data,
            'lot_number': lot_number,
            'model_no': model_no,
            'mac': mac,
            'mfd_date': mfd_date,
            'battery_no': battery_no,
            'battery_mfd_date': battery_mfd_date,
            'assignuser': "itsvenu22@gmail.com"
        }

        print("Request Data:", data)

        response = requests.post(url, json=data)

        print(response.status_code)


        return redirect("login")
        
    else:
        return render(request, "devicereg.html", { 'mac': mac, 'model_no': model_no}) 


def patientreg(request):
    email_data = request.session.get('doctor_email')
    device_data = request.session.get('devicelog')
    error_message = None 
    patient_id = gen_uid()

    if request.method == 'POST':

        patientid_data = request.POST.get('patientid')
        patient_name_data = request.POST.get('patient_name')
        patient_age_data = request.POST.get('patient_age')
        patient_gender_data = request.POST.get('patient_gender')
        contact_data = request.POST.get('contact')
        emergency_data = request.POST.get('emergency')
        height_data = request.POST.get('height')
        weight_data = request.POST.get('weight')
        blood_data = request.POST.get('blood')
        ibw_data = request.POST.get('ibw')
        itv_data = request.POST.get('itv')
        bmi_data = request.POST.get('bmi')
        admitted_date = request.POST.get('admitted_date')
        reason_data = request.POST.get('reason')
        potential_data = request.POST.get('potential')

        url = "http://127.0.0.1:8000/addpatients/"

        data = {
                'deviceid': device_data,
                'doctorid': email_data,
                'patientid': patientid_data,
                'patient_name': patient_name_data,
                'patient_age': patient_age_data,
                'patient_gender': patient_gender_data,
                'height': height_data,
                'weight': weight_data,
                'blood': blood_data,
                'ibw': ibw_data,
                'itv': itv_data,
                'bmi': bmi_data,
                'admitted_date': admitted_date,
                'reason': reason_data,
                'potential': potential_data,
                'contact': contact_data,
                'emergency': emergency_data,
        }

        print("Request Data:", data)

        response = requests.post(url, json=data)

        print(response.status_code)
        print(response.json())
        print('.............................................................')
        print(admitted_date)
        context = request.session.get('context')

        usertype = request.session.get('usertype')
        if usertype == "Superuser":
            return render(request,"superlanding.html", context)
        else:
            return render(request,"landing.html", context)

    else:
        return render(request, "patientreg.html", {'email': email_data, 'patient_id':patient_id, 'device_id': device_data}) 


def mylog(request):
    email_data = request.session.get('doctor_email')
    sno_data = request.session.get('devicelog')

    devices_data = devicedata.objects.values()
    user_data = usermapping.objects.values()

    usertype = request.session.get('usertype')
    print(usertype)
    current_user_id = userdata.objects.filter(email=email_data).values()
    temp = usermapping.objects.filter(user=current_user_id[0]['id']).values()

    mes = [i for i in temp]

    context = {
        'messages': mes[::-1],
        'doctor_email': email_data,
        'device_name': sno_data,
        'usertype': usertype,
    }
    
    return render(request, "mylog.html",context)

def otherlog(request):
    email_data = request.session.get('doctor_email')
    sno_data = request.session.get('devicelog')
    usertype = request.session.get('usertype')
    
    temp = usermapping.objects.all().values()

    print('........................................................')
    mes = [i for i in temp]
    for i in mes:
        t = userdata.objects.filter(id = i['user_id']).values('email')
        i['user_id'] = t[0]['email']
    context = {
        'messages': mes[::-1],
        'doctor_email': email_data,
        'device_name': sno_data,
        'usertype': usertype,
    }
    return render(request, "otherlog.html",context)


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
    sno_data = request.session.get('devicelog')
    usertype = request.session.get('usertype')
    mes = []
    assign_status = "Assign Me"
    devices_data = devicedata.objects.values()
    for i in devices_data:
        if i['assignuser_id'] != None:
            temp = userdata.objects.filter(id=i['assignuser_id']).values()
            assign_status = [j['email'] for j in temp]

            device_id = devicedata.objects.filter(serial_number=i['serial_number']).values()
            user_data = usermapping.objects.filter(device=device_id[0]['id']).values().last()

            i['status'] =  'Idle' if user_data['status'] == False else 'Active'
            i['login_date'] = user_data['login_time'].strftime('%Y-%m-%d')
            i['login_time'] = user_data['login_time'].strftime('%H:%M:%S') if user_data and user_data['login_time'] else None
            keet = userdata.objects.filter(id = user_data['user_id']).values()
            i['last_user'] = keet[0]['email']
        mes.append(i)
        #print(i)


    print(user_data['login_time'].strftime('%Y-%m-%d'))

    context = {
        'messages': mes,
        'doctor_email': email_data,
        'usertype': usertype,
    }

    return render(request, "alldevices.html", context)

def particulardevice(request,pk):
    data = get_object_or_404(devicedata, pk=pk)
    context = {
        "data": data
    }
    return render(request, "particulardevice.html", context)