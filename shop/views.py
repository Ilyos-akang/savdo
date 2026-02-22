

from rest_framework.viewsets import ModelViewSet
from .models import Shop
from .serializer import ShopSerializer

class ShopAPIView(ModelViewSet):
    queryset=Shop.objects.all()
    serializer_class=ShopSerializer