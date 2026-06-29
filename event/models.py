from django.db import models

# Create your models here.
class RegisterDetails(models.Model):
	fullname=models.CharField(max_length=100,default="",null=False)
	address=models.CharField(max_length=100,default="",null=False)
	mobilenumber=models.CharField(max_length=10,default="",null=False)
	emailid=models.CharField(max_length=50,default="",null=False)
	password=models.CharField(max_length=120,default="",null=False)


class RegisterDetails1(models.Model):
	fullname=models.CharField(max_length=100,default="",null=False)
	address=models.CharField(max_length=100,default="",null=False)
	mobilenumber=models.CharField(max_length=15,default="",null=False)
	emailid=models.CharField(max_length=50,default="",null=False)
	password=models.CharField(max_length=120,default="",null=False)

class HallDetails(models.Model):
	venue=models.CharField(max_length=100,default="",null=False)
	contactnumber=models.CharField(max_length=10,default="",null=False)
	

class FoodDetails(models.Model):
	food=models.CharField(max_length=100,default="",null=False)
	plates=models.CharField(max_length=100,default="",null=False)


class ChairDetails(models.Model):
	stagechair=models.CharField(max_length=100,default="",null=False)
	scquantity=models.CharField(max_length=100,default="",null=False)
	chairtype=models.CharField(max_length=100,default="",null=False)
	quantity=models.CharField(max_length=100,default="",null=False)

class DecorationDetails(models.Model):
	theme=models.CharField(max_length=100,default="",null=False)
	eventtype=models.CharField(max_length=100,default="",null=False)
	celebrationspot=models.CharField(max_length=100,default="",null=False)

class SaveDetails(models.Model):
	fullname=models.CharField(max_length=100,default="",null=False)
	mobilenumber=models.CharField(max_length=10,default="",null=False)
	
	quantity=models.CharField(max_length=100,default="",null=False)
	food=models.CharField(max_length=100,default="",null=False)
	plates=models.CharField(max_length=100,default="",null=False)
	venue=models.CharField(max_length=100,default="",null=False)
	theme=models.CharField(max_length=100,default="",null=False)
	eventtype=models.CharField(max_length=100,default="",null=False)
	date=models.CharField(max_length=100,default="",null=False)









