from django.shortcuts import render

import pandas as pd

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    head = []
    rows = []
    with open('inflation_russia.csv', encoding="utf8") as f:
        head = (f.readline().split(';'))
        for line in f:
            cols = [float(x) if x else '' for x in line.split(';')]
            cols[0] = int(cols[0])
            rows.append(cols)

    context = {'head': head
               , 'rows': rows
               }

    return render(request, template_name,
                  context)