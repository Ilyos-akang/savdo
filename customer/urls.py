from rest_framework.routers import DefaultRouter
from .import views

r=DefaultRouter()

r.register('',views.CustomerAPIView)
r.register('order',views.CustomeOrderAPIView)
r.register('order-items',views.CustomeOrderItemsAPIView)
r.register('cart',views.CustomeCartAPIView)

urlpatterns=r.urls