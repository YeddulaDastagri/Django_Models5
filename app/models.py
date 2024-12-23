from django.db import models

# Create your models here. 
class Parent(models.Model):
    fname=models.CharField(max_length=100) 
    lname=models.CharField(max_length=100) 
    p_id=models.IntegerField(primary_key=True) 
    age=models.IntegerField()  
class Child(models.Model):
    p_id=models.ForeignKey(Parent,on_delete=models.CASCADE) 
    fname=models.CharField(max_length=100)  
    lname=models.CharField(max_length=100)
    c_id=models.IntegerField(primary_key=True)  
    age=models.IntegerField()
   
