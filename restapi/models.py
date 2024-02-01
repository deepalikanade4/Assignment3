from django.db import models

class UserData(models.Model):
    UserID=models.IntegerField()
    Name=models.CharField(max_length=70)
    EmailID=models.EmailField(max_length=255)
    Designation=models.CharField(max_length=255)
    