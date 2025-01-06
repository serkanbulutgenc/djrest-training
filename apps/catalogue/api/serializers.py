from rest_framework import serializers
from apps.catalogue.models import Product 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__'

    def create(self, validated_data):
        print('serializer create', validated_data)
        return super().create(validated_data)
    


'''

class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    description = serializers.CharField()

'''