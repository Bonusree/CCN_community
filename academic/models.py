from django.db import models


class Session(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    session_name = models.CharField(max_length=100)

class Department(models.Model):
    department = models.CharField(max_length=100, null=True, unique=True)

class Syllabus(models.Model):
    syllabus = models.ForeignKey('Session', on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdf/')

    
class Routine(models.Model):
    routine = models.ForeignKey('Session', on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdf/')
    
class Question_bank(models.Model):
    question = models.ForeignKey('Session', on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdf/')
    
