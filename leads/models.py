from django.db import models

# Create your models here.


class Leads(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
