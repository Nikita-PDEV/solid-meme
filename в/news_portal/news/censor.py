from django import template

register = template.Library()

@register.filter
def censor_filter(value):
    if not isinstance(value, str):
        raise ValueError("Фильтр применяется только к строковым значениям.")
    
    bad_words = ['редиска', 'редиски', 'Редиска', "Редиски", 'редиске', 'Редиске', 'РеДиСкА',]  # Здесь добавлять другие ругательства
    for word in bad_words:
        value = value.replace(word, '*' * len(word))
    return value