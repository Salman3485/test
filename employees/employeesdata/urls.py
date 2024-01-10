from django.urls import path
from .views import employee_form

urlpatterns = [
       path('employees-form/',employee_form,
    name='employee_form'),
]

