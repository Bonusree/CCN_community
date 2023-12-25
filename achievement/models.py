from django.db import models

# Create your models here.
class Achievement(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_achieved = models.DateField()
    image = models.ImageField(upload_to='achievement_images/', null=True, blank=True)

    def __str__(self):
        return self.title