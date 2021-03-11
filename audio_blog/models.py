from django.db import models
from django.shortcuts import redirect
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
    audio = models.FileField(verbose_name='Аудио', upload_to="music/")
    genres = models.ManyToManyField(Genre, verbose_name='Жанры', blank=True, related_name='audios')

    def get_absolute_url(self):
        return '/'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Аудио"
        verbose_name_plural = "Аудио"
