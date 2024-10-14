from django.db import models #type:ignore
class user(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

def __str__(self):
    return self.username,self.email,self.password





