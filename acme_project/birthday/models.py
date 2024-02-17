from django.db import models
# Импортируем функцию reverse() для получения ссылки на объект.
from django.urls import reverse

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
    image = models.ImageField(
        'Фото',
        blank=True,
        upload_to='birthdays_images'
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

    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})