from django.db import models
from django.conf import settings



class Shop(models.Model):
    super_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=50)
    title=models.TextField()
    logo=models.ImageField(upload_to='shop/images',blank=True,null=True)
    phone_number=models.CharField(max_length=20,blank=True,null=True)

    class Currency(models.TextChoices):
        USD='usd','AQSH dollari'
        UZS='uzs',"O'zbekiston so'mi"
        RUBL='rubl','Rossiya rubli'

    currency=models.CharField(max_length=20,choices=Currency.choices,default=Currency.UZS)
    tax=models.IntegerField(default=0)
    created_at=models.DateField(auto_now=True)
