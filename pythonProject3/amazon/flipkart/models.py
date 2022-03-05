from django.db import models
class employ(models.Model):
    mother=models.CharField(max_length=20)
    father=models.CharField(max_length=30)
    address=models.TextField()
# Create your models here.
