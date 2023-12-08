from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    patient_id = models.AutoField(primary_key=True,unique=True)
    age = models.IntegerField()
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
    doc_name = models.CharField(max_length=255, null=True)
    device = models.ForeignKey('Ventilator', on_delete=models.SET_NULL, null=True, blank=True)


class Ventilator(models.Model):
    STATUS_CHOICES = (
        ('allocated', 'Allocated'),
        ('Not allocated', 'Not Allocated'),
    )
    #email =models.EmailField()
    serial_number = models.CharField(max_length=50, unique=True)
    #is_available = models.BooleanField(default=True)
    #assigned_to = models.CharField(max_length=100, null=True, blank=True)   
    location = models.CharField(max_length=100, null=True, blank=True) 
    model = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not allocated')

class mydevices(models.Model):
    email = models.EmailField(max_length=255,null=True)
    serial_number = models.CharField(max_length=50, unique=False)

    
    





