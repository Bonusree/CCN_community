from django.db import models
from academic.models import Department

# Notice model to store notices with a PDF file
class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    pdf = models.FileField(upload_to='notices/')  

    def __str__(self):
        return self.title
