from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.DecimalField(label="Стоимость товара")
    rate = forms.DecimalField(label="Процентная ставка (в %)",
                              max_value=100,
                              min_value=0,
                              decimal_places=2,
                              max_digits=5)
    months_count = forms.IntegerField(label="Срок кредита в месяцах",
                              max_value=20*12,
                              min_value=3
                                      )

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")
        return initial_fee

    def clean_rate(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        rate = self.cleaned_data.get('rate')
        if not rate:
            raise forms.ValidationError("Не указана процентная ставка")
        return rate

    def clean_months_count(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        months_count = self.cleaned_data.get('months_count')
        if not months_count:
            raise forms.ValidationError("Необходимо указать срок кредита")
        return months_count

    def clean(self):
        # общая функция валидации
        return self.cleaned_data
