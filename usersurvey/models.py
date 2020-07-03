from django.db import models

# Create your models here.


class Survey(models.Model):
    foodquality = models.CharField(max_length=50)
    servicequality = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    comment = models.TextField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email
