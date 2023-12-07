from rest_framework import serializers
from aerodevice.models import patientdata

class patientdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = patientdata
        fields = '__all__'