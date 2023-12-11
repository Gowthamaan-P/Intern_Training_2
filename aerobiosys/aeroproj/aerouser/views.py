from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import userdata
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail

def login(request):
    #template = userdata.objects.all().values()
    template = loader.get_template('login.html')
    context = {
    'udatas': template,
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    error_message = None 
    if request.method == 'POST':
        # Assuming you receive data through a POST request
        field1_data = request.POST.get('username')  
        field2_data = request.POST.get('email')   
        field3_data = request.POST.get('password')
       
        if userdata.objects.filter(email=field2_data).exists():
            error_message = "Email already exists in the database."
            return render(request, "signup.html", {'error_message': error_message})
        else:
            hashed_password = make_password(field3_data)
            new_entry = userdata(username=field1_data, email=field2_data, password=hashed_password)
            new_entry.save()
            subject = 'Welcome to Aerobiosys'
            message = f'Hi {field1_data}, thank you for signing up with Aerobiosys. This is your One Time Password'
            email_from = settings.EMAIL_HOST_USER
            print(field2_data)
            recipient_list = [field2_data]
            send_mail( subject, message, email_from, recipient_list )  
            return HttpResponse("Signup successful")
    else:
        return render(request, "signup.html", {'error_message': error_message}) 

