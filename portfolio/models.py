from django.db import models

class usereg(models.Model):
    uname=models.CharField(max_length=150)
    uemail=models.CharField(max_length=150)
    upassword=models.CharField(max_length=150)
    uabout=models.CharField(max_length=150)
class personaldetails(models.Model):
    tosession=models.CharField(max_length=150)
    uname=models.CharField(max_length=150)
    udob=models.CharField(max_length=150)
    ucontact=models.CharField(max_length=150)
    uemail=models.CharField(max_length=150)
    uaddress=models.CharField(max_length=150)
    uabout=models.CharField(max_length=150)
class educationdetails(models.Model):
    tosession=models.CharField(max_length=150)
    upostgraduate=models.CharField(max_length=150)
    uundergraduate=models.CharField(max_length=150)
    uhighersecondary=models.CharField(max_length=150)
    uhighschool=models.CharField(max_length=150)
class skillset(models.Model):
    tosession=models.CharField(max_length=150)
    uskill1=models.CharField(max_length=150)
    uskill2=models.CharField(max_length=150)
    uskill3=models.CharField(max_length=150)
    uskill4=models.CharField(max_length=150)
class achievement(models.Model):
    tosession=models.CharField(max_length=150)
    uachievement1=models.CharField(max_length=150)
    uachievement2=models.CharField(max_length=150)
    uachievement3=models.CharField(max_length=150)
class experien(models.Model):
    tosession=models.CharField(max_length=150)
    uexp1=models.CharField(max_length=150)
    uexp2=models.CharField(max_length=150)
    uexp3=models.CharField(max_length=150)
class referen(models.Model):
    tosession=models.CharField(max_length=150)
    uref1=models.CharField(max_length=150)
    uref2=models.CharField(max_length=150)