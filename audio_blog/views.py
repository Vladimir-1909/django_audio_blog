from django.views.generic import ListView, DetailView, CreateView
from .models import Audio, Genre


class AudioView(ListView):
    """Список аудио"""
    model = Audio
    paginate_by = 2

    def get_queryset(self):
        queryset = super(AudioView, self).get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            return queryset.filter(name__icontains=search_query)
        return queryset


class GenreView(ListView):
    """Список жанров"""
    model = Genre


class GenreDetail(DetailView):
    """Список аудио жанров"""
    model = Genre
    slug_field = 'url'


class AudioCreate(CreateView):
    """Добавление аудио"""
    model = Audio

    fields = ["name", "audio", "genres"]
