from django.db import models

# Create your models here.


class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name #Iska meaning ye hai ki Employee object ke badle ab name likha hua aayega
    
class Role(models.Model):
    name=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name

class Employee(models.Model):
    First_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()
    
    def __str__(self):
        return "%s %s %s" %(self.First_name,self.last_name,self.phone)
    