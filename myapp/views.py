from .models import Device
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from myapp.serializers import DeviceSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_data(request):

    if request.method == 'GET':
        data = Device.objects.all()
        serializer = DeviceSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        parsed_data = JSONParser().parse(request)
        data = parsed_data.get("data")
        meta_data = parsed_data.get("device")

        serializer = DeviceSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)
