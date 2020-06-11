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

reviewed_products = []

def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)

    form = ReviewForm
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():  # All validation rules pass
            r = Review(
                product=product,
                text=form.cleaned_data['text']
            )
            r.save()
            reviewed_products.append(product.id)
            """
            if 'reviewed_products' in  request.session:
                request.session['reviewed_products'].append(product.id)
            else:
                request.session['reviewed_products'] = [product.id]
            """
            return redirect("product_detail", pk=product.id)

    request.session['reviewed_products'] = reviewed_products
    context = {
        'form': form,
        'product': product
    }

    context['reviews'] = Review.objects.all().filter(product=product)
    context['is_review_exist'] = product.id in request.session['reviewed_products']

    return render(request, template, context)
