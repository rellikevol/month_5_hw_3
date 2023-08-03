from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value):
    if len(value) != 13:
        raise ValidationError(
            _('Длинна телефонного номера не корректна')
        )
    elif value[:4] != '+996':
        raise ValidationError(
            _('Номер должен начинаться с кода региона')
        )


class PhoneNumberField(models.TextField):
    default_validators = [validate_phone_number]


class User(AbstractUser):
    phone_number = PhoneNumberField(max_length=13, verbose_name='Номер телефона')
    age = models.IntegerField(verbose_name="Возраст", default=0)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
