from django.db import models

from .validators import real_age


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
    # Валидатор указывается в описании поля.
    birthday = models.DateField(
        'Дата рождения',
        validators=(real_age,)
    )

    class Meta:
        # проверка на уникальность записи
        # В этом классе указывается перечень полей,
        # совокупность которых должна быть уникальна;
        # имя ограничения.
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'second_name', 'birthday'),
                name='Unique person constraint',
            ),
        )