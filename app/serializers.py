from rest_framework import serializers
from .models import *


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        exclude = ['createdAt', 'updatedAt', 'id']
 
class CropSerializer(serializers.ModelSerializer):
    producerId = ProducerSerializer()
    class Meta:
        model = Crop
        exclude = ['createdAt', 'updatedAt', 'id']

class CropReportSerializer(serializers.ModelSerializer):
    producerId = ProducerSerializer()
    cropId = CropSerializer()
    class Meta:
        model = CropReports
        exclude = ['createdAt', 'updatedAt', 'id']


