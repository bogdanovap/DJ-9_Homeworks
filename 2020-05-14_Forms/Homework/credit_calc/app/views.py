from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"

    form = CalcForm(request.GET)
    context = {
        'form': form
    }
    if form.is_valid():
        price = form.cleaned_data['initial_fee']
        rate = form.cleaned_data['rate']
        months_count = form.cleaned_data['months_count']
        final_price = price+(price*(rate/100))*months_count
        per_month = final_price / months_count
        context['common_result'] = final_price
        context['result'] = per_month

    #form = CalcForm

    return render(request, template, context)
