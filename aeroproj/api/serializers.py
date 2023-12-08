from rest_framework import serializers
from aerodevice.models import devicedata, patientdata, usermapping

class devicedataSerializer(serializers.ModelSerializer):
    class Meta:
        model = devicedata
        fields = '__all__'

class patientdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = patientdata
        fields = '__all__'

class usermappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = usermapping
        fields = '__all__'
