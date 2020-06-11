import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket
from app.utils import get_cities


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    results = []
    cur_val = request.GET.get("term")
    for city in get_cities().filter(name__contains=cur_val):
        results.append(city.name)
    return JsonResponse(results, safe=False)
