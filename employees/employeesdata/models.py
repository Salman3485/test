from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_id = models.CharField(max_length=10)
    Emp_name=models.CharField(max_length=100)
    Emp_salary=models.DecimalField(max_length=10,decimal_places=2)
    Emp_education=models.CharField(max_length=100)
    