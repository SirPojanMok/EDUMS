from django.db import models
from django.contrib.auth.models import User
from stores.models import Seller
from django.utils import timezone

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images', default="noimage.jpg")
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    publishedDate = models.DateTimeField('date published')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    @property
    def is_published_today(self):
        return self.publishedDate.day == timezone.now().day

class Tag(models.Model):

    def __str__(self):
        return self.name

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)

class Transaction(models.Model):

    def __str__(self):

        return str(self.buyer) + ' bought ' + self.item + ' from ' + str(self.seller) + ' at ' + str(self.boughtDate)
    
    item = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)
    total = models.FloatField()
    boughtDate = models.DateTimeField('transaction time')
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)




