from django.shortcuts import render, redirect

from djangoProject2.CompanyAPI.forms import CompanyForm, CompanyEditForm, CompanyDeleteForm, EmployeeForm, \
    EmployeeEditForm, EmployeeDeleteForm
from djangoProject2.CompanyAPI.models import Company, Employee


def CreateCompany(request):

    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CompanyForm(request.POST)

    context = {
        'form' : form
    }

    return render(request,'CreateCompany.html',context)

def EditCompany(request ,pk):

    company = Company.objects.get(pk=pk)
    if request.method == "POST":
        form = CompanyEditForm(request.POST,request.FILES ,instance= company)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CompanyEditForm(instance=company)

    context = {
        'form': form
    }
    return render(request, 'EditCompany.html', context)

def DeleteCompany(request,pk):

    company = Company.objects.get(pk=pk)
    if request.method == "POST":
        form = CompanyDeleteForm(request.POST,request.FILES ,instance= company)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CompanyDeleteForm(instance=company)

    context = {
        'form': form
    }

    return render(request, 'DeleteCompany.html', context)

def AddEmployee(request):

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm(request.POST)

    context = {
        'form' : form
    }

    return render(request, 'AddEmployee.html', context)

def EditEmployee(request,pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == "POST":
        form = EmployeeEditForm(request.POST,request.FILES ,instance= employee)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeEditForm(instance=employee)

    context = {
        'form': form
    }
    return render(request, 'EditEmployee.html', context)

def DeleteEmployee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == "POST":
        form = EmployeeDeleteForm(request.POST,request.FILES ,instance= employee)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeDeleteForm(instance=employee)

    context = {
        'form': form,
    }

    return render(request, 'DeleteEmployee.html', context)
