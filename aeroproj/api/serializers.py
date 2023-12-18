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

class logdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = usermapping
        fields = '__all__'

class usermappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = usermapping
        fields = '__all__'
'''
class PostSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_author(self, obj):
        return obj.author.username
    
    def get_status(self, obj):
        return STATUS[obj.status][1]        
'''