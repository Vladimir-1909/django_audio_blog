from django import template
from ..models import Genre

register = template.Library()


@register.simple_tag()
def get_genres():
    """Вывод всех жанров"""
    return Genre.objects.all()
