from django.shortcuts import render
from .models import Human


def human(request):
    a = Human.objects.get(id=1)
    return render(request, 'homework2/page.html', {'human': a})
