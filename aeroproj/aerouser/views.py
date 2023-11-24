from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import userdata
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.core.mail import send_mail
import uuid, time, pyotp

def gen_uid():
    otp = pyotp.TOTP('base32secret3232')
    return otp.now()

def signup(request):
    error_message = None 
    if request.method == 'POST':
        
        #u_id = uuid.uuid4().hex
        u_id = gen_uid()

        field1_data = request.POST.get('username')  
        field2_data = request.POST.get('email')   
        field3_data = request.POST.get('password')
       
        if userdata.objects.filter(email=field2_data).exists():
        
            error_message = "Email already exists in the database."
            return render(request, "signup.html", {'error_message': error_message})
        
        else:
            request.session['email'] = field2_data
            hashed_password = make_password(field3_data)
            new_entry = userdata(username=field1_data, email=field2_data, password=hashed_password, otp=u_id)
            new_entry.save()


            subject = 'Welcome to Aerobiosys'
            message = f'Hi {field1_data}, thank you for signing up with Aerobiosys. This is your One Time Password : {u_id}'
            email_from = settings.EMAIL_HOST_USER
            print(field2_data)
            recipient_list = [field2_data]
            send_mail( subject, message, email_from, recipient_list )  
            
            return redirect('otp')


        
    else:
        return render(request, "signup.html", {'error_message': error_message}) 


def otp(request):
    user_email = request.session.get('email')
    error_message = None 
    
    if request.method == 'POST':

        entered_otp = request.POST.get('otp')

        if user_email:
            try:
                user_data = userdata.objects.get(email=user_email)
                stored_otp = user_data.otp
                
                if entered_otp == str(stored_otp):

                    return HttpResponse("OTP verified successfully")
                
                else:
                    return render(request,"otp.html")
                
            except userdata.DoesNotExist:
                error_message = "User not found or email not available."
        else:
            error_message = "User email not available in session."

    else:
        return render(request, "otp.html", {'error_message': error_message}) 



def login(request):
    error_message = None 
    if request.method == 'POST':
        field1_data = request.POST.get('email')   
        field2_data = request.POST.get('password')
        
        if not userdata.objects.filter(email__iexact=field1_data).exists():
            error_message = "Email dosen't exists in the database."
            print("email no exsist")
            return render(request, "login.html", {'error_message': error_message})
            
        else:  
            user = userdata.objects.get(email=field1_data)
            stored_password = user.password

            if not check_password(field2_data,stored_password):
                error_message = "wrong password"
                return render(request, "login.html", {'error_message': error_message})
            else:
                return render(request,"landing/landing.html")
    else:
        return render(request, "login.html", {'error_message': error_message})
    

    