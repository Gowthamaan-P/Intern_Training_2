from rest_framework.response import Response
from rest_framework.decorators import api_view
from aerodevice.models import devicedata, patientdata, usermapping
from .serializers import patientdataSerializer, devicedataSerializer, usermappingSerializer

@api_view(['GET'])
def getData(request):
    items = patientdata.objects.all()
    serializer = patientdataSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPatients(request):
    serializer = patientdataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addDevices(request):
    serializer = devicedataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
