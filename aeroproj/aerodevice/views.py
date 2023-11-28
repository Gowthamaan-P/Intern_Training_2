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

    email_data = request.session.get('email')
    error_message = None 
    
    if request.method == 'POST':

        serial_data = request.POST.get('serial_number')  
        model_data = request.POST.get('model')
        location_data = request.POST.get('location')
        status_data = "Idle"

        new_entry = devicedata(userid=email_data, model=model_data, 
                            serial_number=serial_data, status=status_data, location=location_data)
        new_entry.save()
        return redirect("login")
        
    else:
        return render(request, "devicereg.html", {'email': email_data}) 


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
            return redirect("devicereg")
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

def devices(request):
    email_data = request.session.get('email')

    objects = devicedata.objects.filter(userid=email_data).values()

    #return render(request, "usercheck.html", {'': error_message})
    return HttpResponse(email_data)

def patients(request):
    email_data = request.session.get('email')   
    return HttpResponse(email_data)