from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Seller(models.Model):
    
    def __str__(self):
        return str(self.user)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.CharField(max_length=20)
