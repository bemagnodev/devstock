from rest_framework import viewsets
from .models import EndomarketingStock, GeneralSuppliesStock, ActionsStock
from .serializers import EndomarketingStockSerializer, CleaningProductsStockSerializer, ActionsStockSerializer  
class EndomarketingStockViewSet(viewsets.ModelViewSet):
    queryset = EndomarketingStock.objects.all()
    serializer_class = EndomarketingStockSerializer

class CleaningProductsStockViewSet(viewsets.ModelViewSet):
    queryset = GeneralSuppliesStock.objects.all()
    serializer_class = CleaningProductsStockSerializer

class ActionsStockViewSet(viewsets.ModelViewSet):
    queryset = ActionsStock.objects.all()
    serializer_class = ActionsStockSerializer