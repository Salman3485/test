from django.shortcuts import render
from.forms import EmployeeForm
from .models import Employee                                           #not montioned

# Create your views here.

def employee_form(request):
   if request.method=='POST':
       form = EmployeeForm(request.POST)
       if form.is_valid():
           form.save()
   else:
           
     form=EmployeeForm()
     return render(request,'employee_form.html',{'form':form})
           