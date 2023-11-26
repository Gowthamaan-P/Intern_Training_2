from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import userdata
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.core.mail import send_mail
import uuid, time, pyotp
from django.contrib import messages


def gen_uid():
    otp = pyotp.TOTP('base32secret3232')
    return otp.now()

def signup(request):
    error_message = None 
    if request.method == 'POST':
        
        u_id = gen_uid()

        field1_data = request.POST.get('username')  
        field2_data = request.POST.get('email')   
        field3_data = request.POST.get('password')
       
        if userdata.objects.filter(email=field2_data).exists():
        
            error_message = "Email already exists in the database."
            return render(request, "signup.html", {'error_message': error_message})
        
        else:
            request.session['username'] = field1_data
            request.session['email'] = field2_data
            request.session['password'] = field3_data
            request.session['otp'] = u_id
            


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
    user_name = request.session.get('username')
    user_password = request.session.get('password')
    user_otp = request.session.get('otp')
    error_message = None 
    
    if request.method == 'POST':

        entered_otp = request.POST.get('otp')

        if user_email:
            try:
                
                if entered_otp == user_otp:
                    hashed_password = make_password(user_password)
                    new_entry = userdata(username=user_name, email=user_email, password=hashed_password)
                    new_entry.save()
                    login(request)
                
                else:
                    messages.success(request, "Incorrect OTP")
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
            error_message1 = "Incorrect Email!"
            print("email no exsist")

            messages.success(request, "signup")

            return render(request, "login.html", {'error_message1': error_message1},)
            
        else:  
            user = userdata.objects.get(email=field1_data)
            stored_password = user.password

            if not check_password(field2_data,stored_password):
                error_message1 = "Incorrect password!"
                messages.success(request, "forgot")
                
                return render(request, "login.html", {'error_message1': error_message1},)
            else:
                return render(request,"landing.html")
    else:
        return render(request, "login.html", {'error_message': error_message})
    
def forgot_otp(request,user_email):

    user_otp = request.session.get('otp')
    user_new_pwd = request.session.get('password')
    error_message = None 
    
    if request.method == 'POST':

        entered_otp = request.POST.get('otp')

        if user_email:
            try:
                
                if entered_otp == user_otp:
                    t = userdata.objects.get(email=user_email)
                    t.value = user_new_pwd
                    t.save()
                    login(request)
                
                else:
                    messages.success(request, "Incorrect OTP")
                    return render(request,"otp.html")
                
            except userdata.DoesNotExist:
                error_message = "User not found or email not available."
        else:
            error_message = "User email not available in session."

    else:
        return render(request, "forgototp.html", {'error_message': error_message}) 

def forgot(request):
    error_message = None 
    if request.method == 'POST':
        field1_data = request.POST.get('email')   
        
        if not userdata.objects.filter(email__iexact=field1_data).exists():
            error_message1 = "Incorrect Email!"
            print("email no exsist")

            messages.success(request, "signup")

            return render(request, "forgot.html", {'error_message1': error_message1})
        
        else:
            u_id = gen_uid()

            subject = 'Security Alert'
            message = f'Hi {field1_data}.This is your One Time Password : {u_id}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [field1_data]
            send_mail( subject, message, email_from, recipient_list )  

            forgot_otp(request)
        
    else:
        return render(request, "forgot.html", {'error_message': error_message})