from django.db import models
from aerouser.models import userdata

class devicedata(models.Model):

    device_name = models.CharField(max_length=255,null=True)
    model = models.CharField(max_length=255,null=True)
    serial_number = models.CharField(max_length=255,null=True)
    lot_number = models.IntegerField(null=True)
    model_no = models.CharField(max_length=255,null=True)
    mac = models.CharField(max_length=255,null=True)
    mfd_date = models.DateTimeField(null=True, blank=True)
    battery_no = models.CharField(max_length=255,null=True)
    battery_mfd_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20,null=True)
    location = models.CharField(max_length=255,null=True)
    assignuser = models.ForeignKey(userdata, on_delete=models.SET_NULL, null=True, blank=True)
    #assignstatus = models.CharField(max_length=255,null=False)

class patientdata(models.Model):

    deviceid = models.CharField(max_length=255,null=False)
    doctorid = models.CharField(max_length=255,null=False)
    patientid = models.CharField(max_length=255,null=False)
    patient_name = models.CharField(max_length=255,null=False)
    patient_age = models.IntegerField(null=False)
    patient_gender = models.CharField(max_length=255,null=False)
    height = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    blood = models.CharField(max_length=255,null=False)
    ibw = models.IntegerField(null=False)
    itv = models.IntegerField(null=False)
    bmi = models.IntegerField(null=False)
    admitted_date = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=255,null=False)
    potential = models.CharField(max_length=255,null=False)
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
