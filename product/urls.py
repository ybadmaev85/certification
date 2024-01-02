from django.urls import path

from product.apps import ProductConfig
from rest_framework.routers import DefaultRouter

from product.views import SupplierViewSet, ProducerAPIView, ProducerCreateAPIView, ProducerRetrieveAPIView, \
    ProducerUpdateAPIView, ProducerDestroyAPIView

app_name = ProductConfig

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')
urlpatterns = [

    path('producer/', ProducerAPIView.as_view(), name='producer_list'),
    path('producer/create', ProducerCreateAPIView.as_view(), name='producer_create'),
    path('producer/<int:pk>', ProducerRetrieveAPIView.as_view(), name='producer_get'),
    path('producer/update/<int:pk>', ProducerUpdateAPIView.as_view(), name='producer_update'),
    path('producer/delete/<int:pk>', ProducerDestroyAPIView.as_view(), name='producer_delete'),

] + router.urls
