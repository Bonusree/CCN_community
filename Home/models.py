from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ForeignKey relationship with User model
    profession = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    isAlumni = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username  # You can change this to display a relevant field
