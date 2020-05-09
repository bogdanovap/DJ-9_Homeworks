from django import template

from datetime import datetime

register = template.Library()


@register.filter
def format_selftext(value, count):
    words = value.split(" ")
    if len(words) < 2*count + 1:
        return value
    else:
        res = " ".join(words[:count])
        res += " ... "
        res += " ".join(words[-count:])
        return res

@register.filter
def format_date(value):
    # Ваш код
    diff_minutes = (datetime.now().timestamp()-value)/60/60
    if diff_minutes < 10:
        return "только что"
    elif diff_minutes < 24*60:
        return f"{diff_minutes/24:.0f} час назад"
    else:
        return datetime.fromtimestamp(value).strftime("yyyy-MM-dd")


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value, default):
    if not value:
        return default
    elif value<=-5:
        return "Все плохо"
    elif value<=5:
        return "Нейтрально"
    else:
        return "Хорошо"

@register.filter
def format_num_comments(value):
    # Ваш код
    if value == 0:
        return "Оставьте комментарий"
    if value > 50:
        return "50+"
    else:
        return value



