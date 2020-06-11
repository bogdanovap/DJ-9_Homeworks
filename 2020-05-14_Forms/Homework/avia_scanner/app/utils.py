from django.core.cache import cache

from app.models import City

CITIES_CACHE_TIMEOUT = 60


def get_cities():
    cache_key = 'city:cities-list'
    res = cache.get(cache_key)
    if not res:
        res = City.objects.all()
        cache.set(cache_key, res, timeout=CITIES_CACHE_TIMEOUT)
    return res
