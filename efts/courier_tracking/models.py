from django.db import models

# Create your models here.
class courier_booking(models.Model):
    CourierId = models.IntegerField()
    From_Name = models.CharField(max_length = 20)
    From_EmailAddress = models.CharField(max_length = 40)
    From_Gender = models.CharField(max_length = 10)
    From_Age = models.CharField(max_length = 10)
    From_Address = models.CharField(max_length = 30)
    From_Mobile = models.CharField(max_length = 20)
    To_Name = models.CharField(max_length = 20) 
    To_Gender = models.CharField(max_length = 10) 
    To_Address = models.CharField(max_length = 30)
    To_Mobile = models.CharField(max_length = 20)
    Product_Name = models.CharField(max_length = 20)
    Weight = models.CharField(max_length = 10)
    Price = models.CharField(max_length = 10)

    
class billing(models.Model):
    Courier_Id = models.CharField(max_length = 10)
    From_Name = models.CharField(max_length = 20)
    Product_Name = models.IntegerField(max_length = 30)
    Weight = models.CharField(max_length = 10)
    Price = models.CharField(max_length = 10)
    
    