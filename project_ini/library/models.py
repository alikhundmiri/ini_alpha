from django.db import models


class genre(models.Model):
    genre_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.genre_name

class books(models.Model):
    g = models.ForeignKey(genre, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    y_o_publish = models.DateTimeField()
    y_o_upload = models.DateTimeField()

    def __str__(self):
        return self.title + ", " + self.author

