from django.db import models
import uuid

class member(models.Model):
    Name=models.CharField(max_length=200)
    Category=models.CharField(max_length=200)
    Amount=models.IntegerField()
    created_by=models.CharField(max_length=100)
    


    def __str__(self):
        return self.Name