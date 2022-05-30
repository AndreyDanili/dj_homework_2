# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorsInfoSerializer


class ListCreateAPIView(APIView):
    def get(self, request):
        all_sensors = Sensor.objects.all()
        result = SensorsInfoSerializer(all_sensors, many=True)
        return Response(result.data)

    def post(self, request):
        result = request.data
        Sensor.objects.create(name=result['name'], description=result['description'])
        return Response({'message': 'OK'})


class RetrieveUpdateAPIView(APIView):
    def get(self, request, sensor_id):
        sensor_info = Sensor.objects.filter(id__exact=sensor_id)
        result = SensorDetailSerializer(sensor_info, many=True)
        return Response(result.data)

    def patch(self, request, sensor_id):
        result = request.data
        Sensor.objects.filter(id__exact=sensor_id).update(description=result['description'])
        return Response({'message': 'OK'})


class MeasurementAPIView(APIView):
    def post(self, request):
        result = request.data
        if request.GET.get('image'):
            Measurement.objects.create(sensor_id=result['sensor'], temperature=result['temperature'], image=request.data['image'])
        else:
            Measurement.objects.create(sensor_id=result['sensor'], temperature=result['temperature'])
        return Response({'message': 'OK'})
