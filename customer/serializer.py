from .models import CustomeCart,CustomeOrder,   CustomeOrderItems,Customer
from rest_framework.serializers import ModelSerializer

class CustomerSerializer(ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"



class CustomerCartSerializer(ModelSerializer):
    class Meta:
        model=CustomeCart
        fields="__all__"


class CustomerOrderSerializer(ModelSerializer):
     class Meta:
        model=CustomeOrder
        fields="__all__"



class CustomerOrderItemsSerializer(ModelSerializer):
     class Meta:
        model=CustomeOrderItems
        fields="__all__"
