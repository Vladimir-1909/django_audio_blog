from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Жанр", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse('genre_detail', kwargs={'slug': self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Audio(models.Model):
    """Аудио"""
    name = models.CharField(verbose_name='Название', max_length=125)
    date = models.DateTimeField(auto_now_add=True)
    audio = models.FileField(upload_to="music/")
    genres = models.ManyToManyField(Genre, blank=True, related_name='audios')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Аудио"
        verbose_name_plural = "Аудио"
