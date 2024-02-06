from django.db import models
from django.contrib.auth.models import User


class Product (models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    price=models.IntegerField()
    img= models.ImageField(null=True)
    def _str_(self):
        return self.name
    @property
    def imgURL(self):
        try:
            url=self.img.url
        except:
            url=''
        return url

    def __str__(self):
        return self.name
    
class Cart (models.Model):
    id=models.AutoField(primary_key=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=200)
    img=models.FileField(upload_to='static/media/images/', default='path/to/default/image.jpg')
    category=models.CharField(max_length=200)
    price=models.IntegerField()

    def __str__(self):
        return self.name
# Create your models here.
    

class CartItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='cart/images/')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
