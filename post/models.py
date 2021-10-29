from django.db import models


class PostModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return f'{self.title}, {self.description[:10]}'
