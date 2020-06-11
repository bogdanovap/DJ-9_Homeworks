from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


key_name = 'reviewed_products'


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    if key_name in request.session:
        reviewed_products = request.session.get(key_name)
    else:
        request.session[key_name] = []
        reviewed_products = []

    form = ReviewForm
    if request.method == 'POST' and not(product.id in reviewed_products):
        form = ReviewForm(request.POST)
        if form.is_valid():  # All validation rules pass
            r = Review(
                product=product,
                text=form.cleaned_data['text']
            )
            r.save()
            reviewed_products.append(product.id)

    request.session[key_name] = reviewed_products

    print(reviewed_products)
    print(request.session[key_name])
    context = {
        'form': form,
        'product': product
    }

    context['reviews'] = Review.objects.all().filter(product=product)
    context['is_review_exist'] = product.id in request.session['reviewed_products']

    return render(request, template, context)
