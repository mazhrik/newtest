from django.db import models

# Create your models here.




# class Employee(models.Model):
#     """ Name of the employee """
#     first_name = models.TextField()
#     last_name = models.TextField()
#     position = models.TextField()
#     salary = models.IntegerField(default=0)
#     age = models.IntegerField(default=0)
#     # department =  models.CharField(default='',max_length=225,)
#     department = models.ForeignKey(DepartmentName, on_delete=models.CASCADE, related_name='employee_department')
#     # def __str__(self):
#     #     return self.first_name
   

# class Department(models.Model):
#     department = models.ForeignKey(DepartmentName, on_delete=models.CASCADE, related_name='department_name')
#     cheif=models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='chief', editable=True)
#     # employees=models.ForeignKey(Employee,related_name='employees_dep_list',on_delete=models.CASCADE)
#     # def __str__(self):
#     #     return self.department.name
    
# class Company(models.Model):
#     company_departments=models.ForeignKey(DepartmentName,on_delete=models.CASCADE, related_name='deparments',default='')
#     def __str__(self):
#         return self.company_name

class Employee(models.Model):
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')
    position = models.TextField(default='')
    salary = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    department = models.ForeignKey("Department",on_delete=models.CASCADE, related_name='deparments',blank=True, null=True)
    def __str__(self):
        return self.first_name
    class Meta:
        permissions = [
            ("view_employee_list","view_employee_list"),
            ]    


class Department(models.Model):
    name = models.CharField(max_length = 100,default='')
    chief_employee = models.OneToOneField(Employee,on_delete=models.CASCADE, related_name='employee',default='',blank=True, null=True)
    List_employee = models.ManyToManyField(Employee, related_name='empl',default=' ')
    def __str__(self):
        return self.name
  


class Company(models.Model):
    name = models.CharField(max_length = 100,default='')
    departments = models.ManyToManyField(Department, related_name='dep',default='',blank=True, null=True)
    def __str__(self):
        return self.name