from django import forms


class BirthdayForm(forms.Form):
    first_name = forms.CharField(
        label='Имя',
        max_length=50
    )
    second_name = forms.CharField(
        label='Фамилия',
        required=False,
        help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
