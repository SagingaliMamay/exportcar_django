from django.db import models


# Create your models here.

class Car_data(models.Model):
    mark = models.CharField(max_length=15)
    year = models.IntegerField()
    nrg = models.CharField(max_length=15)
    transmission = models.CharField(max_length=15)
    km = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=800)
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=30)
    tel = models.CharField(max_length=20)
    photo = models.ImageField(null=True, blank=True, upload_to="images/%Y/%m/%d")
    send_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mark

