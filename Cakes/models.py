from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Chef(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=10)
    county = models.CharField(max_length=50)
    constituency = models.CharField(max_length=50)
    ward = models.CharField(max_length=50)
    sub_area = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Cake(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    cake_name = models.CharField(max_length=50)
    cake_image = models.FileField()

    def __str__(self):
        return self.cake_name
