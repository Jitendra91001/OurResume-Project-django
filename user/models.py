from django.db import models

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=100)
    ppic = models.ImageField(upload_to='static/profile/',default="")
    dec = models.TextField(max_length=5000)
    def __str__(self):
        return self.name

class skill(models.Model):
    pname = models.CharField(max_length=100)
    pdate = models.DateField()
    def __str__(self):
        return self.pname

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80, primary_key=True)
    mobile = models.CharField(max_length=20)
    massage = models.TextField(max_length=2000)

class resume(models.Model):
    rpic = models.ImageField(upload_to='static/resume/', default="")
    rdate= models.DateField()


class certificate(models.Model):
    cname=models.CharField(max_length=100)
    cpic = models.ImageField(upload_to='static/certificate/', default="")
    rdate = models.DateField()

