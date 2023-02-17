from django.core.exceptions import ValidationError


def validate_only_letters(input):

    for char in input :
        if not char.isalpha():
            raise  ValidationError ("Ensure this value contains only letters.")

def validate_only_positive_num(input):

    if input <= 0 :
        raise  ValidationError("Number has to be positive !")



