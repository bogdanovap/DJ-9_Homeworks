from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from users.models import User
from .models import Comment, Article
from .models import Merchandise
from .models import Order, OrderDetails


def index_view(request):
    template_name = 'istore\\index.html'
    context = {
        "articles": Article.objects.all().order_by("-creation_date")
    }

    return render(request, template_name, context)


PRODUCTS_PER_PAGE = 2


def catalog_view(request, cat_id: int = 0):
    template_name = 'istore\\catalog.html'

    products_all = Merchandise.objects.all().filter(category_id=cat_id)
    paginator = Paginator(products_all, PRODUCTS_PER_PAGE)

    current_page = request.GET.get('page', 1)
    products = paginator.get_page(current_page)

    prev_page_url, next_page_url = None, None
    if products.has_next():
        next_page_url = f"?page={products.next_page_number()}"
    if products.has_previous():
        prev_page_url = f"?page={products.previous_page_number()}"

    context = {
        "products": products,
        "next": next_page_url,
        "prev": prev_page_url,
    }

    return render(request, template_name, context)


def product_view(request, slug):
    # TODO: add anonymous comments
    template_name = 'istore\\product.html'
    product = Merchandise.objects.get(slug=slug)
    context = {
        'product': product,
        'comments': Comment.objects.all().filter(product=product)
    }

    return render(request, template_name, context)


@login_required
def add_to_cart(request, slug):
    prod = Merchandise.objects.all().filter(slug=slug)
    print(prod)
    if len(prod) == 1:
        order, created = Order.objects.get_or_create(user=request.user, active=True)
        order_det, created = OrderDetails.objects.get_or_create(order=order, product=prod[0])
        order_det.quantity += 1
        order_det.save()
    return redirect('cart')


@login_required
def buy_all(request, order_id):
    order = Order.objects.get(id=order_id)
    order.active = False
    order.save()
    return redirect('cart')


@login_required
def cart_view(request):
    template_name = "istore\\cart.html"
    context = {}
    user = User.objects.get(email=request.user)
    order = Order.objects.all().filter(user=user)
    order = order.filter(active=True)
    print(order)
    if order:
        prods_in_order = OrderDetails.objects.all().filter(order=order[0])
        context['prods_in_order'] = prods_in_order
        context['order'] = order[0]

    return render(request, template_name, context)
