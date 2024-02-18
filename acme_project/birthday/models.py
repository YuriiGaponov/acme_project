from django.db import models
# Импортируем функцию reverse() для получения ссылки на объект.
from django.urls import reverse
from django.contrib.auth import get_user_model

from .validators import real_age

# Да, именно так всегда и ссылаемся на модель пользователя!
User = get_user_model()


class Tag(models.Model):
    tag = models.CharField(
        'Тег',
        max_length=20
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return self.tag


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
    author = models.ForeignKey(
        User,
        verbose_name='Автор записи',
        on_delete=models.CASCADE,
        null=True
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True,
        help_text='Удерживайте Ctrl для выбора нескольких вариантов'
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


class Congratulation(models.Model):
    text = models.TextField('Текст поздравления')
    birthday = models.ForeignKey(
        Birthday, 
        on_delete=models.CASCADE,
        related_name='congratulations',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)
