from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
# admin.site.register(EmployeeHistory)
admin.site.register(Company)