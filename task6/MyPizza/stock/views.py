from django.shortcuts import render
from .models import Pizza


def index(request):
    list_of_active_pizzas = ''
    for p in Pizza.objects.all():
        if p.active:
            list_of_active_pizzas = list_of_active_pizzas + ' ' + p.__str__()

    return render(request, 'index.html', {'list': list_of_active_pizzas})
