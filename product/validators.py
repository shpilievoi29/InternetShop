from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def positive_validator(value):
    if value < 0.00:
        raise ValidationError("Should be positive or zero")

    return value
