from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# def home(request):
#     return HttpResponse('<h1>Hello, Home</h1>')

user1 = {
    'name': 'bob',
    'surname': 'johnson',
    'age': 40
}


def home(request):
    return render(request, 'myfirstapp/home.html', {'context': user1})


def pers(request):
    p1 = Person.objects.get(id=1)
    return render(request, 'myfirstapp/home.html', {'context': p1})






#
# def about(request):
#     return HttpResponse('<h1>About Page</h1>')
#
#
# def home(request):
#     user1 = {
#         'name': 'bob',
#         'surname': 'johnson',
#         'age': 40
#     }
#     return render(request, 'myfirstapp/home.html', user1)
