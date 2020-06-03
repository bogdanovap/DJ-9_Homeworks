from django.shortcuts import render

from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort','name')
    qs = Phone.objects.all();
    data = qs.order_by('name')
    if sort =='min_price':
        data = qs.order_by('price')
    elif sort =='max_price':
        data = qs.order_by('-price')
    context = {"phones" : data}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    print("slug is: "+slug)
    data = Phone.objects.get(slug = slug)
    context = {"phone" : data}
    return render(request, template, context)
