from rest_framework.routers import DefaultRouter
from .views import ProductAPIView,ProductInputAPIView,CategoryAPIView

r=DefaultRouter()

r.register(r"category",CategoryAPIView)
r.register(r"product",ProductAPIView)
r.register(r"product-input",ProductInputAPIView)

urlpatterns=r.urls