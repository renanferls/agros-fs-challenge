from django.db.models import ProtectedError
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Crop, CropReports, Producer
from .serializers import *


# Create your views here.

class ProducerView(APIView):

    def get(self, request, pk=None):
        if pk is None:
            query = Producer.objects.all()
            serializer = ProducerSerializer(query, many=True)
            return Response(serializer.data)
        
        try:
            query = Producer.objects.get(id=pk)
            serializer = ProducerSerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Producer.DoesNotExist:
            return Response(
                {'message': f'Producer with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)
    

    def post(self, request, format=None):

        serializer = ProducerSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    def put(self, request, pk):
        
        try:
            producerItem = Producer.objects.get(id=pk)
            serializer = ProducerSerializer(producerItem, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Producer.DoesNotExist:
            return Response(
                {'message': f'Producer with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)       
                

    def delete(self, request, pk):
        
        try:
            producerItem = Producer.objects.get(id=pk)
            producerItem.delete()
            return Response(
                {'message': f'Producer with id {pk} was successfully deleted'}, 
                status=status.HTTP_200_OK)

        except Producer.DoesNotExist:
            return Response(
                {'message': f'Producer with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)
        
        except ProtectedError:
            return Response(
                {'message': f'Producer with id {pk} cannot be deleted, some instances refers to it'}, 
                status=status.HTTP_406_NOT_ACCEPTABLE)


class CropView(APIView):

    def get(self, request, pk=None):
        if pk is None:
            query = Crop.objects.all()
            serializer = CropSerializer(query, many=True)
            return Response(serializer.data)
        
        try:
            query = Crop.objects.get(id=pk)
            serializer = CropSerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Crop.DoesNotExist:
            return Response(
                {'message': f'Crop with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)
    

    def post(self, request, format=None):

        serializer = CropSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    def put(self, request, pk):
        
        try:
            cropItem = Crop.objects.get(id=pk)
            serializer = CropSerializer(cropItem, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Crop.DoesNotExist:
            return Response(
                {'message': f'Crop with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)       
                

    def delete(self, request, pk):
        
        try:
            cropItem = Crop.objects.get(id=pk)
            cropItem.delete()
            return Response(
                {'message': f'Crop with id {pk} was successfully deleted'}, 
                status=status.HTTP_200_OK)

        except Crop.DoesNotExist:
            return Response(
                {'message': f'Crop with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)
        
        except ProtectedError:
            return Response(
                {'message': f'Crop with id {pk} cannot be deleted, some instances refers to it'}, 
                status=status.HTTP_406_NOT_ACCEPTABLE)


class CropReportView(APIView):

    def get(self, request, pk=None):
        if pk is None:
            query = CropReports.objects.all()
            serializer = CropReportSerializer(query, many=True)
            return Response(serializer.data)
        
        try:
            query = CropReports.objects.get(id=pk)
            serializer = CropReportSerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except CropReports.DoesNotExist:
            return Response(
                {'message': f'Crop Report with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)
    

    def post(self, request, format=None):

        serializer = CropReportSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    def put(self, request, pk):
        
        try:
            cropReportItem = Producer.objects.get(id=pk)
            serializer = CropReportSerializer(cropReportItem, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        except CropReports.DoesNotExist:
            return Response(
                {'message': f'Crop Report with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)       
                

    def delete(self, request, pk):
        
        try:
            cropReportItem = Crop.objects.get(id=pk)
            cropReportItem.delete()
            return Response(
                {'message': f'Crop Report with id {pk} was successfully deleted'}, 
                status=status.HTTP_200_OK)

        except CropReports.DoesNotExist:
            return Response(
                {'message': f'Crop Report with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)
        
        except ProtectedError:
            return Response(
                {'message': f'Crop Report with id {pk} cannot be deleted, some instances refers to it'}, 
                status=status.HTTP_406_NOT_ACCEPTABLE)
