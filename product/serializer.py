from rest_framework.serializers import ModelSerializer
from .models import Product,ProductInput ,Category

class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class ProductInputSerializer(ModelSerializer):
     class Meta:
        model=ProductInput
        fields='__all__'
        



class CategorySerializer(ModelSerializer):
     class Meta:
        model=Category
        fields='__all__'
