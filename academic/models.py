from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    session_name = models.CharField(max_length=100)
    
class Faculty(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    faculty_name = models.CharField(max_length=100)

class Department(models.Model):
    department = models.CharField(max_length=100, null=True, unique=True)

class Syllabus(models.Model):
    syllabus = models.ForeignKey('Session', on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdf/')

class Routine(models.Model):
    routine = models.ForeignKey('Session', on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdf/')


class Question_bank(models.Model):
    session = models.ForeignKey('Session', on_delete=models.CASCADE,null=True)
    faculty=models.ForeignKey('Faculty', on_delete=models.CASCADE,null=True)
    course_name = models.CharField(max_length=100,null=True)
    course_code = models.CharField(max_length=100,null=True)
    pdf_file = models.FileField(upload_to='pdf/')
    
class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    course_name = models.CharField(max_length=100, null=True)
    course_code = models.CharField(max_length=100,null=True)
    video_url = models.URLField(max_length=200)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

