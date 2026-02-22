from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN='admin','Admin'
        CLIENT='client','Client'
        SELLER='seller','Seller'
        MANAGER='manager','Manager'
        WAREHOUSE_WORKER='warehouse_worker','Warehouse worker'


    phone_number=models.CharField(max_length=20,blank=True,null=True)
    role=models.CharField(max_length=30,choices=Role.choices,default=Role.CLIENT)


    def __str__(self):
        return self.username