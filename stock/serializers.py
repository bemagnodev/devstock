from rest_framework import serializers
from .models import EndomarketingStock, GeneralSuppliesStock, ActionsStock

class EndomarketingStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndomarketingStock
        fields = '__all__'

class CleaningProductsStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSuppliesStock
        fields = '__all__'

class ActionsStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionsStock
        fields = '__all__'