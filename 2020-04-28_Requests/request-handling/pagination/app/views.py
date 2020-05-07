from django.shortcuts import render_to_response, redirect
from django.urls import reverse

import csv
from django.core.paginator import Paginator
from django.conf import settings

import pandas as pd

def load_data():
    #print(settings.BUS_STATION_CSV)
    df = pd.read_csv(settings.BUS_STATION_CSV,encoding='cp1251')
    #print(df.head())
    data = df[['Name', 'Street', 'District']].to_dict('records')
    #print(data.head())
    return data


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = request.GET.get('page', 1)

    paginator = Paginator(load_data(), 10)
    bus_stations = paginator.get_page(current_page)

    prev_page_url, next_page_url = None, None
    if bus_stations.has_previous():
        #print('has previous: ',bus_stations.previous_page_number())
        prev_page_url = f"?page={bus_stations.previous_page_number()}"
    if bus_stations.has_next():
        #print('has next',bus_stations.next_page_number())
        next_page_url = f"?page={bus_stations.next_page_number()}"

    return render_to_response('index.html', context={
        'bus_stations': bus_stations,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

