"""Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from istore.views import add_to_cart, cart_view, buy_all
from istore.views import index_view, catalog_view, product_view
from users.views import signup

urlpatterns = [
    path('', index_view, name='index'),
    path('catalog/<int:cat_id>', catalog_view, name='catalog_view'),
    path('catalog/<slug:slug>', product_view, name='product_view'),

    path('cart/', cart_view, name='cart'),
    path('cart/<int:order_id>', buy_all, name='buy_all'),
    path('cart/<slug:slug>', add_to_cart, name='add_to_cart'),

    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', signup, name="signup"),

    path('admin/', admin.site.urls),
]

# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls'))
# ]
