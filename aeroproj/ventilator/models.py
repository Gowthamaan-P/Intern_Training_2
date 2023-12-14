from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    patient_id = models.AutoField(primary_key=True,unique=True)
    age = models.IntegerField(null= True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    STATUS_CHOICES = [
        ('PASSIVE', 'Passive'),
        ('EMERGENCY', 'Emergency'),
        ('DISCHARGED', 'Discharged'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PASSIVE')
    doc_id = models.CharField(max_length=255)  # Link to userdata model
    doc_name = models.CharField(max_length=255, null=True)
    device = models.ForeignKey('Ventilator', on_delete=models.SET_NULL, null=True, blank=True)


class Ventilator(models.Model):
    STATUS_CHOICES = (
        ('allocated', 'Allocated'),
        ('Not allocated', 'Not Allocated'),
    )
    serial_number = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=100, null=True, blank=True) 
    model = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not allocated')

class device_logs(models.Model):
    log_id = models.AutoField(primary_key=True,unique=True)
    serial_number = models.CharField(max_length=50)
    device_log_in = models.DateTimeField(null=True, blank=True)
    device_log_out = models.DateTimeField(null=True, blank=True)
    assigned_by_doc_id = models.CharField(max_length=255) 
    assigned_to_patient_id = models.CharField(max_length=255)



class mydevices(models.Model):
    email = models.EmailField(max_length=255,null=True)
    serial_number = models.CharField(max_length=50, unique=False)

    
    





