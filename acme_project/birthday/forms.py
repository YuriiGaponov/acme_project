from django import forms
# Импортируем класс ошибки валидации.
from django.core.exceptions import ValidationError
# Импорт функции для отправки почты.
from django.core.mail import send_mail

# Импортируем класс модели Birthday.
from .models import Birthday, Congratulation

# Множество с именами участников Ливерпульской четвёрки.
BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # # Указываем, что надо отобразить все поля.
        # fields = '__all__'
        exclude = ('author',)
        # Чтобы форма работала как раньше — нужно указать, что для поля
        # с датой рождения используется виджет с типом данных date.
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        # Разбиваем полученную строку по пробелам 
        # и возвращаем только первое имя.
        return first_name.split()[0]

    def clean(self):
        # Вызов родительского метода clean.
        super().clean()
        # Получаем имя и фамилию из очищенных полей формы.
        first_name = self.cleaned_data['first_name']
        second_name = self.cleaned_data['second_name']
        # Проверяем вхождение сочетания имени и фамилии во множество имён.
        if f'{first_name} {second_name}' in BEATLES:
            # Отправляем письмо, если кто-то представляется 
            # именем одного из участников Beatles.
            send_mail(
                subject='Another Beatles member',
                message=f'{first_name} {second_name} пытался опубликовать запись!',
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=True,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )


class CongratulationForm(forms.ModelForm):

    class Meta:
        model = Congratulation
        fields = ('text',)
