from rest_framework.response import Response
from rest_framework.decorators import api_view
from aerodevice.models import patientdata
from .serializers import patientdataSerializer

@api_view(['GET'])
def getData(request):
    items = patientdata.objects.all()
    serializer = patientdataSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = patientdataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)