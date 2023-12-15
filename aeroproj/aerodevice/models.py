from django.db import models
from aerouser.models import userdata

class devicedata(models.Model):

    device_name = models.CharField(max_length=255,null=False)
    model = models.CharField(max_length=255,null=False)
    serial_number = models.CharField(max_length=255,null=False)
    status = models.CharField(max_length=20,null=False)
    location = models.CharField(max_length=255,null=False)
    assignuser = models.ForeignKey(userdata, on_delete=models.SET_NULL, null=True, blank=True)
    #assignstatus = models.CharField(max_length=255,null=False)

class patientdata(models.Model):

    doctorid = models.CharField(max_length=255,null=False)
    patientid = models.CharField(max_length=255,null=False)
    patient_name = models.CharField(max_length=255,null=False)
    patient_age = models.IntegerField(null=False)
    patient_gender = models.CharField(max_length=255,null=False)
    contact = models.IntegerField(null=False)
    emergency = models.CharField(max_length=10,null=False)  

class usermapping(models.Model):
    user = models.ForeignKey(userdata, on_delete=models.SET_NULL, null=True, blank=True)
    device = models.ForeignKey(devicedata, on_delete=models.SET_NULL, null=True, blank=True)
    login_time = models.DateTimeField(null=True, blank=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)


class Post(models.Model):
    pass
