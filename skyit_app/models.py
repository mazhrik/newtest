from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    position = models.TextField()
    salary = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    department =  models.CharField(default='',max_length=225,)
   

class Department(models.Model):
    department_name = models.ForeignKey(Employee)
    cheif=models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='chief', editable=True)
    employees=models.ManyToManyField(Employee,related_name='employees_dep_list')
    
class Company(models.Model):
    company_name = models.CharField(max_length=225)
    departments=models.ManyToManyField(Department)
