from django.db import models


class Birthday(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=50
    )
    second_name = models.CharField(
        'Фамилия',
        blank=True,
        help_text='Необязательное поле',
        max_length=50
    )
    birthday = models.DateField(
        'Дата рождения'
    )