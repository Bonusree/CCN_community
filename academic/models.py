from django.db import models

# Create your models here.
class Syllabus:
    department = models.CharField(max_length=100,null=True)
    session = models.CharField(max_length=100,null=True)
    pdf_file = models.FileField(upload_to='pdf/')
