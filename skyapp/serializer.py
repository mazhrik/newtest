import json
from rest_framework import serializers
# from .models import vechile_m, date_vehicle
from .models import Employee, Company ,Department
from rest_framework.serializers import SerializerMethodField
from django.core.serializers import serialize
from django.http import JsonResponse
class Employee_serializer(serializers.ModelSerializer):
    dep_name = SerializerMethodField('get_dep_name', allow_null=True, read_only=True)
    def get_dep_name(self, obj):
        try:
           
            dep=obj.department.name
            return dep
          
        except:
            return None
    class Meta:
        model = Employee
        fields = ('first_name','last_name','position','salary','age','dep_name')


class Company_serializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class Department_serializer(serializers.ModelSerializer):
    chief_name = SerializerMethodField('get_chief_name', allow_null=True, read_only=True)
    list_emp = SerializerMethodField('get_list_emp', allow_null=True, read_only=True)

    def get_chief_name(self, obj):
        try:
            
            chiefname=obj.chief_employee.first_name + obj.chief_employee.last_name
            return chiefname
        except:
            return None
    def get_list_emp(self, obj):
        try:
         
            employee=list(obj.List_employee.all().values())
      
            return employee
          
        except:
            return None
    class Meta:
        model = Department
        fields = ('id','name','chief_name','list_emp')


