from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)

"""
Person.objects.create(first_name='ani', last_name='amir')
Person.objects.create(first_name='john', last_name='john')
Person.objects.get(first_name='ani')
Person.objects.filter(first_name='ani')
Person.objects.all()
"""
# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=100)


class Address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

# class Musician(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     instrument = models.CharField(max_length=100)


# class Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField(max_length=5)


# class Person(models.Model):
#     SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#     name = models.CharField(max_length=60)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


# class Owner(models.Model):
#     name = models.CharField()
#     surname = models.CharField()
#
#
# class Dog(models.Model):
#
#     name = models.CharField()
#     owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
#     breed = models.TextField()
#     age = models.IntegerField(default=1)


from django.utils import timezone
from mysite import settings


# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title

