from .models import Ventilator,Patient,mydevices,device_logs
from django.http import HttpResponseServerError
from django.shortcuts import render, get_object_or_404,redirect
from aerouser.models import userdata
import requests
from datetime import datetime
from django.db.models import Max

def device_reg2(request):
    if request.method == 'POST':
        serial_number = request.POST.get('serial_number')
        location = request.POST.get('location')
        model = request.POST.get('model')
        status='Not allocated'
        url = "http://127.0.0.1:8000/adddevices"

        data = {
            'serial_number':serial_number,
            'location':location,
            'model':model,
            'status':status  
        }
        
        response = requests.post(url, json=data)  
        # note 1:converts Python dictionary data into JSON.
        # note 2:The conversion to JSON format is essential when transmitting data over HTTP.
        print(response.status_code)

        error_message="Device Saved."
        return render(request, "device_reg2.html",{'error_message': error_message})
    else:
        return render(request, "device_reg2.html")
    

def patient_data(request, serial_number1):
    if request.method == 'POST':
        name = request.POST.get('patient_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        field1_data = request.session.get('email')
        field2_data = request.session.get('serial_number')
        user = userdata.objects.get(email=field1_data)
        doc_name = user.username
        doc_id = user.doctor_id
        
        
        ventilator_instance = get_object_or_404(Ventilator, serial_number=serial_number1)

        max_patient_id = Patient.objects.aggregate(Max('patient_id'))['patient_id__max']
        if max_patient_id is None:
            patient_id = 1
        else:
            patient_id = max_patient_id + 1

        max_log_id = device_logs.objects.aggregate(Max('log_id'))['log_id__max']
        if max_log_id is None:
            log_id = 1
        else:
            log_id = max_log_id + 1
        
        request.session['log_id'] = log_id


        new_entry = Patient(
            name=name,
            patient_id=patient_id,
            doc_name=doc_name,
            age=age,
            gender=gender,
            device=ventilator_instance,
            doc_id=doc_id
        )
        new_entry.save()

        ventilator_instance.status = 'Allocated'
        ventilator_instance.save()

        new_device_log_entry = device_logs(
            log_id=log_id,
            serial_number=serial_number1,
            device_log_in=datetime.now(),  
            device_log_out=None,   
            assigned_by_doc_id=doc_id,
            assigned_to_patient_id=patient_id
        )
        new_device_log_entry.save()
        
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
    

"""
def patient_data(request, serial_number1):
    if request.method == 'POST':
        name = request.POST.get('patient_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        field1_data = request.session.get('email')
        field2_data = request.session.get('serial_number')
        user = userdata.objects.get(email=field1_data)
        doc_name = user.username
        doc_id = user.doctor_id
        
        ventilator_instance = get_object_or_404(Ventilator, serial_number=serial_number1)

        max_patient_id = Patient.objects.aggregate(Max('patient_id'))['patient_id__max']
        if max_patient_id is None:
            patient_id = 1
        else:
            patient_id = max_patient_id + 1

        new_entry = Patient(
            name=name,
            patient_id=patient_id,
            doc_name=doc_name,
            age=age,
            gender=gender,
            device=ventilator_instance,
            doc_id=doc_id
        )
        new_entry.save()

        ventilator_instance.status = 'Allocated'
        ventilator_instance.save()

        new_device_log_entry = device_logs(
            serial_number=serial_number1,
            device_log_in=datetime.now(),  
            device_log_out=None,   
            assigned_by_doc_id=doc_id,
            assigned_to_patient_id=patient_id
        )
        new_device_log_entry.save()
        
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
            return HttpResponseServerError('Internal Server Error')"""



def remove_device(request, serial_number2):
    try:
        device = Ventilator.objects.get(serial_number=serial_number2)
        device.status = 'Not allocated'
        device.save()
        
        id = request.session.get('log_id')
        device_log_entry=device_logs.objects.get(log_id=id)
        device_log_entry.device_log_out=datetime.now()
        device_log_entry.save()


        patient = Patient.objects.filter(device=device).first()

        if patient:

            patient.status = 'Discharged'
            patient.save()

        return redirect('device_list')  
    except Ventilator.DoesNotExist:
        return HttpResponseServerError('Device not found')  
    except Exception as e:
        return HttpResponseServerError(f'Error: {str(e)}')


    
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

def device_logs_view(request):
    if request.method == 'GET':
        all_logs = device_logs.objects.all()
        return render(request, 'device_logs.html', {'device_logs': all_logs})
    else:
        return render(request, "landing.html") 
