from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import devicedata, patientdata
from aerouser.models import userdata
#from aerodevice.views import login
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.core.mail import send_mail
import uuid, time, pyotp
from django.contrib import messages

def devicereg(request):

    #email_data = request.session.get('email')
    error_message = None 
    
    if request.method == 'POST':

        d_name = request.POST.get('device_name')
        serial_data = request.POST.get('serial_number')  
        model_data = request.POST.get('model')
        location_data = request.POST.get('location')
        status_data = "Idle"

        new_entry = devicedata(device_name=d_name, model=model_data, 
                            serial_number=serial_data, status=status_data, location=location_data)
        new_entry.save()
        return redirect("login")
        
    else:
        return render(request, "devicereg.html",) 


def usercheck(request):
    error_message = None 
    if request.method == 'POST':
        email_data = request.POST.get('email')   
        
        if not userdata.objects.filter(email__iexact=email_data).exists():
            error_message1 = "Incorrect Email!"
            print("email no exsist")

            messages.success(request, "Incorrect Email!")

            return render(request, "signup.html", {'error_message1': error_message1})
            
        else:  
            request.session['email'] = email_data
            return redirect("mydevices")

    else:
        return render(request, "usercheck.html", {'error_message': error_message})
    
def patientreg(request):
    email_data = request.session.get('email')
    error_message = None 
    
    if request.method == 'POST':

        patientid_data = request.POST.get('patientid')
        patient_name_data = request.POST.get('patient_name')
        patient_age_data = request.POST.get('patient_age')
        patient_gender_data = request.POST.get('patient_gender')
        contact_data = request.POST.get('contact')
        emergency_data = request.POST.get('emergency')

        new_entry = patientdata(doctorid = email_data,patientid = patientid_data,
                    patient_name = patient_name_data, patient_age = patient_age_data,
                    patient_gender = patient_gender_data,contact = contact_data, emergency = emergency_data)
        new_entry.save()
        return redirect("login")
        
    else:
        return render(request, "patientreg.html", {'email': email_data}) 



def patientcheck(request):
    error_message = None 
    if request.method == 'POST':
        email_data = request.POST.get('email')   
        
        if not userdata.objects.filter(email__iexact=email_data).exists():
            error_message1 = "Incorrect Email!"
            print("email no exsist")

            messages.success(request, "Incorrect Email!")

            return render(request, "signup.html", {'error_message1': error_message1})
            
        else:  
            request.session['email'] = email_data
            return redirect("patientreg")
    else:
        return render(request, "usercheck.html", {'error_message': error_message})

def mydevices(request):
    email_data = request.session.get('email')

    user_instance = userdata.objects.get(email=email_data)
    devices_data = devicedata.objects.filter(assignuser=user_instance).values()
    


    return render(request, "mydevices.html", {'doctor_email': email_data },)

def patients(request):
    email_data = request.session.get('doctor_email')

    objects = devicedata.objects.filter(assignuser=email_data).values()

    return render(request, "mydevices.html", {'doctor_email': objects })


def alldevices(request):
    email_data = request.session.get('doctor_email')

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
    }

    return render(request, "alldevices.html", context)