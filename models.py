from django.db import models
import django.core.validators as django_validators

from djangoProject2.CompanyAPI.validators.InputValidators import validate_only_letters, validate_only_positive_num


class Company(models.Model):
    NAME_MIN_LEN = 3
    NAME_MAX_LEN = 30
    DESCRIPTION_MAX_LEN = 300

    company_name = models.CharField(

        max_length=NAME_MAX_LEN,
        validators=(
            django_validators.MinLengthValidator(NAME_MIN_LEN),
        ),
    )

    company_logo = models.URLField(

        blank=True,
        null=True,
    )

    company_description = models.TextField(

        max_length=DESCRIPTION_MAX_LEN,
        blank=True,
    )



class Employee(models.Model):
    NAME_MIN_LEN = 2
    NAME_MAX_LEN = 15
    POSITIONFIELD_MAX_LEN = 20

    first_name = models.CharField(

        max_length=NAME_MAX_LEN,
        validators=(
            django_validators.MinLengthValidator(NAME_MIN_LEN),
            validate_only_letters,
        ),
    )
    last_name = models.CharField(

        max_length=NAME_MAX_LEN,
        validators=(
            django_validators.MinLengthValidator(NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    date_of_birth = models.DateField(

    )

    photo = models.URLField(
        null= True,
        blank= True
    )
    position = models.CharField(
        max_length=POSITIONFIELD_MAX_LEN,
        validators=(validate_only_letters,),
    )

    salary = models.FloatField(
        default= 0,
        validators=(
            validate_only_positive_num,
        )

    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,

    )