from django.db import models

class Student(models.Model):
    sn = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    age = models.IntegerField(default=0)
    roll = models.IntegerField(default=0)
    address = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name