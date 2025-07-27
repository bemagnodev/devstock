from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import EndomarketingStockViewSet, CleaningProductsStockViewSet, ActionsStockViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'endomarketing', EndomarketingStockViewSet)
router.register(r'cleaning-products', CleaningProductsStockViewSet)
router.register(r'actions', ActionsStockViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
] + router.urls