from django.contrib import admin
from django.urls import path

from djangoProject2.CompanyAPI.views import CreateCompany, EditCompany, DeleteCompany, AddEmployee, EditEmployee, \
    DeleteEmployee

urlpatterns = (
    path('CreateCompany/', CreateCompany,name='create company'),
    path('EditCompany/<int:pk>/', EditCompany,name='edit company'),
    path('DeleteCompany/<int:pk>/', DeleteCompany,name='delete company'),

    path('AddEmployee/', AddEmployee,name='add employee'),
    path('EditEmployee/<int:pk>/', EditEmployee,name='edit employee'),
    path('DeleteEmployee/<int:pk>/', DeleteEmployee,name='delete employee'),
)