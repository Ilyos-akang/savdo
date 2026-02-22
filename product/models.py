from django.db import models
from django.conf import settings

class Category(models.Model):
    name=models.CharField(max_length=255)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='childern')
    # shop=models.ForeignKey('shop.Shop',on_delete=models.CASCADE,related_name='category_shop')
    title=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    shop=models.ForeignKey('shop.Shop',on_delete=models.RESTRICT,related_name='product_shop',null=True)
    category=models.ForeignKey(Category,on_delete=models.RESTRICT,related_name='product_category',blank=True,null=True)
    name=models.CharField(max_length=255)
    title=models.TextField(blank=True,null=True)
    input_price=models.DecimalField(decimal_places=2,max_digits=15,default=0)
    output_price=models.DecimalField(decimal_places=2,max_digits=15,default=0)
    wholesale_price=models.DecimalField(decimal_places=2,max_digits=15,default=0)
    barcode=models.CharField(blank=True,null=True)
    image=models.ImageField(upload_to='images/product/images',blank=True,null=True)
    stock=models.IntegerField(default=0)
    min_stock=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name
    


class ProductInput(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='product_input')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    quantity=models.IntegerField(default=0)
    supplier=models.CharField(max_length=255,blank=True,null=True)
    new_input_price=models.DecimalField(decimal_places=2,max_digits=15,default=0)
    new_output_price=models.DecimalField(decimal_places=2,max_digits=15,default=0)
    new_wholesale_price=models.DecimalField(decimal_places=2,max_digits=15,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.product.name
    