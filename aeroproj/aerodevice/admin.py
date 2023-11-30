from django.contrib import admin
from .models import devicedata, patientdata,usermapping



admin.site.register(devicedata)
admin.site.register(patientdata)
admin.site.register(usermapping)