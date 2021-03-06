from django.db import models
from django.db.models.enums import Choices
from django_mysql.models import EnumField

# Create your models here.
class student(models.Model):
    user_id=models.CharField(max_length=8,blank=False,null=False,primary_key=True)
    first_name=models.CharField(max_length=15,blank=False,null=False)
    last_name=models.CharField(max_length=15)
    gender=EnumField(choices=['M','F','Other'])
    ph_no=models.CharField(max_length=10,blank=False,null=False)
    par_ph_no=models.CharField(max_length=10,blank=False,null=False)
    yoj=models.CharField(max_length=4,blank=False,null=False)
    yoj=models.CharField(max_length=4,blank=False,null=False)
    dept=EnumField(choices=['CSE','IT','BT','ECE','EEE','MECH','CIVIL','AERO','CHEM'])
    password=models.CharField(max_length=40,blank=False,null=False)
    class Meta:
        managed = True 
        db_table = 'student'

class teacher(models.Model):
    user_id=models.CharField(max_length=8,blank=False,null=False,primary_key=True)
    first_name=models.CharField(max_length=15,blank=False,null=False)
    last_name=models.CharField(max_length=15)
    gender=EnumField(choices=['M','F','Other'])
    ph_no=models.CharField(max_length=10,blank=False,null=False)
    teach_ph_no=models.CharField(max_length=10,blank=False,null=False)
    yoj=models.CharField(max_length=4,blank=False,null=False)
    qualification=EnumField(choices=['UG','PG','PHD'])
    dept=EnumField(choices=['CSE','IT','BT','ECE','EEE','MECH','CIVIL','AERO','CHEM'])
    password=models.CharField(max_length=40,blank=False,null=False)
    class Meta:
        managed = True 
        db_table = 'teacher'