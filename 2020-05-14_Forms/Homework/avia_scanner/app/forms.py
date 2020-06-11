from django import forms

from .widgets import AjaxInputWidget
from .models import City
from app.utils import get_cities


class SearchTicket(forms.Form):
    # Добавьте здесь поля, описанные в задании
    url = "api/city_ajax"
    widget = AjaxInputWidget(url)
    city_from = forms.CharField(widget=widget)
    city_to = forms.ChoiceField(choices=get_cities().values_list())
    travel_date = forms.DateField(widget=forms.SelectDateWidget)
