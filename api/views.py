from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Measurement
from operator import attrgetter


@api_view(['GET'])
def get_min_measurement(request):
    try:
        all_measurements = Measurement.objects.all()
        minimum_measurement = min(
            all_measurements, key=attrgetter('sensor_data'))
        return Response({"min": f'{minimum_measurement}'})
    except Measurement.DoesNotExist:
        return Response(stauts=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_max_measurement(request):
    try:
        all_measurements = Measurement.objects.all()
        maximum_measurement = max(
            all_measurements, key=attrgetter('sensor_data'))
        return Response({"max": f'{maximum_measurement}'})
    except Measurement.DoesNotExist:
        return Response(stauts=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_avg_measurement(request):
    try:
        all_measurements = Measurement.objects.all()
        average_measurement = sum(
            measurement.sensor_data for measurement in all_measurements) / len(all_measurements)
        return Response({"avg": f'{average_measurement}'})
    except Measurement.DoesNotExist:
        return Response(stauts=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def save_measurement(request):
    try:
        json = request.data
        measurements = list(json["sensor_data"])
        for data in measurements:
            measurement = Measurement(sensor_data=data)
            measurement.save()
        return Response({"succes": "true"})
    except Exception as e:
        return Response({"error": "The given data was not correct, please make sure it is a number"})
