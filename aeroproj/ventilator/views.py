from .models import Ventilator,Patient,mydevices
from django.http import HttpResponseServerError
from django.shortcuts import render, get_object_or_404
from aerouser.models import userdata
from django.shortcuts import render,redirect

"""def device_reg(request):
    if request.method == 'POST':
        field1_data = request.POST.get('email')
        request.session['email'] = field1_data
        if not userdata.objects.filter(email__iexact=field1_data).exists():
            error_message = "Please sign up."
            return render(request, "device_reg.html", {'error_message': error_message})
        
        return render(request,"device_reg2.html")
    else:
        return render(request, "device_reg.html")"""

def device_reg2(request):
    if request.method == 'POST':
        serial_number = request.POST.get('serial_number')
        location = request.POST.get('location')
        model = request.POST.get('model')
        new_entry = Ventilator(
            serial_number=serial_number,
            location=location,
            model=model,
            status='Not allocated'  
        )
       
        new_entry.save()
        error_message="Device Saved."
        return render(request, "device_reg2.html",{'error_message': error_message})
    else:
        return render(request, "device_reg2.html")

def patient_data(request, serial_number1):
    if request.method == 'POST':
        name = request.POST.get('patient_name')
        patient_id = request.POST.get('patient_id')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        status = request.POST.get('status')
        field1_data = request.session.get('email')
        field2_data = request.session.get('serial_number')
        user = userdata.objects.get(email=field1_data)
        doc_name = user.username

        # Get the Ventilator instance based on the provided serial number
        
        ventilator_instance = get_object_or_404(Ventilator, serial_number=serial_number1)

        new_entry = Patient(
            name=name,
            patient_id=patient_id,
            age=age,
            gender=gender,
            status=status,
            doc_name=doc_name,
            device=ventilator_instance  # Assign the Ventilator instance to the device field
        )
        new_entry.save()
        
        # Update Ventilator status and create mydevices entry
        ventilator_instance.status = 'Allocated'
        ventilator_instance.save()
        mydevices_entry = mydevices(email=field1_data, serial_number=field2_data)
        mydevices_entry.save()

        return render(request, "landing.html", {'error_message': doc_name, 'error_message1': field2_data})
    else:
        field1_data = request.session.get('serial_number')
        try:
            user = Ventilator.objects.get(serial_number=field1_data)
            if user.status == 'Allocated':
                devices = Ventilator.objects.all() 
                error_message = "This device is already allocated."
                return render(request, "device_list.html", {'devices': devices, 'error_message': error_message})
            else:
                return render(request, "patient.html", {'serial_number': serial_number1})
        except Ventilator.DoesNotExist:
            return HttpResponseServerError('Internal Server Error')


def remove_device(request, serial_number2):
    try:
        # Get the device based on the serial number
        device = Ventilator.objects.get(serial_number=serial_number2)

        # Set the device status to 'Unallocated'
        device.status = 'Not allocated'
        device.save()

        # Find the associated patient for this device using the reverse relationship
        patient = Patient.objects.filter(device=device).first()

        if patient:
            # Update the patient status to 'Discharged'
            patient.status = 'Discharged'
            patient.save()

        return redirect('device_list')  # Replace 'device_list' with your actual device list URL name
    except Ventilator.DoesNotExist:
        return HttpResponseServerError('Device not found')  # Handle device not found error
    except Exception as e:
        return HttpResponseServerError(f'Error: {str(e)}')  # Return the specific error message for debugging



    
def patient_list(request): 
    if request.method == 'GET':
        patients = Patient.objects.all() 
        return render(request, "patient_list.html", {'patients': patients})
    else:
        return render(request, "patient.html") 
    
def device_list(request):
    if request.method == 'GET':
        devices = Ventilator.objects.all()  
        return render(request, "device_list.html", {'devices': devices})
    else:
        return render(request, "patient.html") 

def my_devices(request):
    field1_data = request.session.get('serial_number')
    if request.method == 'GET':
        patients = Patient.objects.all()  
        return render(request, "patient_list.html", {'patients': patients})
    else:
        return render(request, "patient.html") 
