from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Emp_id','Emp_name','Emp_salary','Emp_education']    