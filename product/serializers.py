from rest_framework import serializers

from product.models import Commodity, Producer, Supplier, Supply


class CommoditySerializer(serializers.ModelSerializer):

    class Meta:
        model = Commodity
        fields = '__all__'


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = '__all__'
        read_only_fields = ('debt',)
