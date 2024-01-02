import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, viewsets
from product.models import Producer, Supplier
from product.permissions import IsActiveEmployee
from product.serializers import ProducerSerializer, SupplierSerializer


class ProducerAPIView(generics.ListAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [IsActiveEmployee]


class ProducerCreateAPIView(generics.CreateAPIView):
    serializer_class = ProducerSerializer
    permission_classes = [IsActiveEmployee]


class ProducerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProducerSerializer
    queryset = Producer.objects.all()
    permission_classes = [IsActiveEmployee]


class ProducerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProducerSerializer
    queryset = Producer.objects.all()
    permission_classes = [IsActiveEmployee]


class ProducerDestroyAPIView(generics.DestroyAPIView):
    queryset = Producer.objects.all()
    permission_classes = [IsActiveEmployee]


class SupplierFilter(django_filters.FilterSet):
    """ Фильтр объектов по определенной стране"""
    class Meta:
        model = Supplier
        fields = ['country']


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter
    permission_classes = [IsActiveEmployee]