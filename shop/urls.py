from rest_framework.routers import DefaultRouter
from .views import ShopAPIView

r=DefaultRouter()

r.register(r"",ShopAPIView)

urlpatterns=r.urls