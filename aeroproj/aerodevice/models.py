from django.db import models

class devicedata(models.Model):

    userid = models.CharField(max_length=255,null=False)
    model = models.CharField(max_length=255,null=False)
    serial_number = models.CharField(max_length=255,null=False)
    status = models.CharField(max_length=20,null=False)
    location = models.CharField(max_length=255,null=False)

class patientdata(models.Model):

    doctorid = models.CharField(max_length=255,null=False)
    patientid = models.CharField(max_length=255,null=False)
    patient_name = models.CharField(max_length=255,null=False)
    patient_age = models.IntegerField(null=False)
    patient_gender = models.CharField(max_length=255,null=False)
    contact = models.IntegerField(null=False)
    emergency = models.CharField(max_length=10,null=False)  







