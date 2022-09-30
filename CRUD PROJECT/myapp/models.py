from django.db import models

# Create your models here.
class StudentModel(models.Model):
      no=models.AutoField(primary_key=True)
      name=models.CharField(max_length=70)
      contact=models.IntegerField()
      email=models.EmailField()
      course=models.CharField(max_length=80)
      gender=models.CharField(max_length=70)
      image=models.ImageField(upload_to='Student_Images')

class UserModel(models.Model):
      no=models.IntegerField(primary_key=True)
      name=models.CharField(max_length=79)


