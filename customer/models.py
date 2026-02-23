from django.db import models
from django.conf import settings


class Customer(models.Model):
   
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    shop=models.ForeignKey('shop.Shop',on_delete=models.SET_NULL,null=True)
    full_name=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=30)
    phone_number2=models.CharField(max_length=30)
    info=models.TextField(blank=True,null=True)
    total_debit=models.DecimalField(decimal_places=2,max_digits=15,default=0)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name
    

    
class CustomeCart(models.Model):
    product=models.ForeignKey('product.Product',on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "salom"
    


class CustomeOrder(models.Model):
    shop=models.ForeignKey('shop.Shop',on_delete=models.SET_NULL,null=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    total_price=models.DecimalField(decimal_places=2,max_digits=15,default=0)
    discount_price=models.DecimalField(decimal_places=2,max_digits=15,default=0)


    def __str__(self):
        return self.customer.full_name
    



class CustomeOrderItems(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    total_price=models.DecimalField(decimal_places=2,max_digits=15,default=0,blank=True,null=True)
    discount_price=models.DecimalField(decimal_places=2,max_digits=15,default=0,blank=True,null=True)



    def __str__(self):
        return self.customer.full_name
    