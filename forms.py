import os

from django.forms import models

from djangoProject2.CompanyAPI.models import Company, Employee


class CompanyForm(models.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'



class CompanyEditForm(models.ModelForm):


    class Meta:
        model = Company
        fields = '__all__'


class CompanyDeleteForm(models.ModelForm):

    def save(self, commit=True):
        image_path = self.instance.image.path
        self.instance.delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Company
        fields = ()


    pass



class EmployeeForm(models.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeEditForm(models.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name','last_name','date_of_birth','photo','position','salary')
class EmployeeDeleteForm(models.ModelForm):

    def save(self, commit=True):
        image_path = self.instance.image.path
        self.instance.delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Employee
        fields = ()