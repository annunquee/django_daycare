from django.db import models
from django.contrib.auth import get_user_model

users = get_user_model()

class staff(models.Model):
    students = models.CharField(max_length=100)
    parents =  models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.IntegerField()
    students = models.ForeignKey(users, on_delete=models.CASCADE, related_name='user')