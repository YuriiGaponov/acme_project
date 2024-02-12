from django.shortcuts import render

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


def birthday(request):
    # if request.GET:
    #     form = BirthdayForm(request.GET)
    #     if form.is_valid():
    #         pass
    # else:
    #     form = BirthdayForm()
    # изменить метод GET на POST
    form = BirthdayForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            form.cleaned_data['birthday']
        )
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context=context)


def birthday_list(request):
    # Получаем все объекты модели Birthday из БД.
    birthdays = Birthday.objects.all()
    # Передаём их в контекст шаблона.
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context)
