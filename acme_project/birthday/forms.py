from django import forms

# Импортируем класс модели Birthday.
from .models import Birthday


class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        # Чтобы форма работала как раньше — нужно указать, что для поля
        # с датой рождения используется виджет с типом данных date.
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
