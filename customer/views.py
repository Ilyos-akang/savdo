from rest_framework.viewsets import ModelViewSet
from .models import CustomeCart,CustomeOrder,   CustomeOrderItems,Customer
from .serializer import CustomerSerializer,CustomerOrderSerializer,CustomerCartSerializer,CustomerOrderItemsSerializer


class CustomerAPIView(ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer


class CustomeCartAPIView(ModelViewSet):
    queryset=CustomeCart.objects.all()
    serializer_class=CustomerCartSerializer





class CustomeOrderAPIView(ModelViewSet):
    queryset=CustomeOrder.objects.all()
    serializer_class=CustomerOrderSerializer



class CustomeOrderItemsAPIView(ModelViewSet):
    queryset=CustomeOrderItems.objects.all()
    serializer_class=CustomerOrderItemsSerializer


