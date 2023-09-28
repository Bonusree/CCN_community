from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ForeignKey relationship with User model
    fullName = models.CharField(max_length=100,null=True)
    profession = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    session = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=255,null=True)
    isAlumni = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username  # You can change this to display a relevant field
