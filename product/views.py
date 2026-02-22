from rest_framework.viewsets import  ModelViewSet
from .serializer import ProductSerializer,ProductInputSerializer,CategorySerializer
from .models import Product,ProductInput,Category

class ProductAPIView(ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()



class CategoryAPIView(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer



class ProductInputAPIView(ModelViewSet):
    queryset=ProductInput.objects.all()
    serializer_class=ProductInputSerializer