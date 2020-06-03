from django.shortcuts import render

from phones.models import Phone, Vendor

def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all();
    print(phones)
    context = {"model":Phone._meta.fields, "phones":phones}
    return render(
        request,
        template,
        context
    )
