from django.db.models import ProtectedError
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Crop, CropReports, Producer
from .serializers import *

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
# Create your views here.

# PRODUCERS VIEW

class ProducerListCreate(APIView):
    @extend_schema(
        request=None,
        responses={200: ProducerSerializer},
        description='Retrieve a list of all producers',
        methods=["GET"]
    )
    def get(self, request):
            query = Producer.objects.all()
            serializer = ProducerSerializer(query, many=True)
            return Response(serializer.data)
    
    @extend_schema(
        request=ProducerSerializer,
        responses={201: ProducerSerializer},
        description='Create a new producer',
        methods=["POST"]
    )
    def post(self, request, format=None):        
        serializer = ProducerSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ProducerReadUpdateDelete(APIView):
    @extend_schema(
        request=None,
        responses={200: ProducerSerializer},
        description='Retrieve a single producer',
        methods=["GET"]
    )
    def get(self, request, pk):
        try:
            query = Producer.objects.get(id=pk)
            serializer = ProducerSerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Producer.DoesNotExist:
            return Response(
                {'message': f'Producer with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)
    
    @extend_schema(
        request=ProducerSerializer,
        responses={200: ProducerSerializer},
        description='Update a single producer',
        methods=["PUT"]
    )
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
                
    @extend_schema(
        request=None,
        responses={200: None},
        description='delete a single producer',
        methods=["DELETE"]
    )
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


# CROPS VIEW

class CropListCreate(APIView):
    @extend_schema(
        request=None,
        responses={200: CropSerializer},
        description='Retrieve a list of all crops',
        methods=["GET"]
    )
    def get(self, request):
        query = Crop.objects.all()
        serializer = CropSerializer(query, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        request=CropCreateSerializer,
        responses={200: None},
        description='Create a new crop',
        methods=["POST"]
    )
    def post(self, request, format=None):
        serializer = CropCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CropReadUpdateDelete(APIView):
    @extend_schema(
        request=None,
        responses={200: CropSerializer},
        description='Retrieve a single crop',
        methods=["GET"]
    )
    def get(self, request, pk):        
        try:
            query = Crop.objects.get(id=pk)
            serializer = CropSerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Crop.DoesNotExist:
            return Response(
                {'message': f'Crop with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)
    
    @extend_schema(
        request=CropCreateSerializer,
        responses={200: CropCreateSerializer},
        description='Update a single crop',
        methods=["PUT"]
    )
    def put(self, request, pk):
        try:
            cropItem = Crop.objects.get(id=pk)
            serializer = CropCreateSerializer(cropItem, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Crop.DoesNotExist:
            return Response(
                {'message': f'Crop with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)       

    @extend_schema(
        request=None,
        responses={200: None},
        description='delete a single crop',
        methods=["DELETE"]
    )      
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

class CropReportListCreate(APIView):
    @extend_schema(
        request=None,
        responses={200: CropReportSerializer},
        description='Retrieve a list of all crop reports',
        methods=["GET"]
    )
    def get(self, request):
        query = CropReports.objects.all()
        serializer = CropReportSerializer(query, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        request=CropReportCreateSerializer,
        responses={201: None},
        description='Create a new crop report',
        methods=["POST"]
    )
    def post(self, request, format=None):
        serializer = CropReportCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class CropReportReadUpdateDelete(APIView):
    @extend_schema(
        request=None,
        responses={200: CropReportSerializer},
        description='Retrieve a single crop report',
        methods=["GET"]
    )
    def get(self, request, pk):
        try:
            query = CropReports.objects.get(id=pk)
            serializer = CropReportSerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except CropReports.DoesNotExist:
            return Response(
                {'message': f'Crop Report with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        request=CropReportCreateSerializer,
        responses={200: CropReportCreateSerializer},
        description='Update a single crop report',
        methods=["PUT"]
    )
    def put(self, request, pk):        
        try:
            cropReportItem = Producer.objects.get(id=pk)
            serializer = CropReportCreateSerializer(cropReportItem, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        except CropReports.DoesNotExist:
            return Response(
                {'message': f'Crop Report with id {pk} not found'}, 
                status=status.HTTP_404_NOT_FOUND)       
                
    @extend_schema(
        request=None,
        responses={200: None},
        description='Delete a single crop report',
        methods=["DELETE"]
    )
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
