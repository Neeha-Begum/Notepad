from django.db import models

# Create your models here.
class List(models.Model):
    name=models.CharField(max_length=20)
    contact=models.IntegerField()

    def __str__(self):
        return self.name