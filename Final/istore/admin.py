from django.contrib import admin

from .models import Category, CategoryGroup
from .models import Comment, Article
from .models import Merchandise
from .models import Order, OrderDetails


# TODO: set verbouse names for all fields
# TODO: set verbouse names (meta) for all models

@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'description']
    # search_fields = ['car__brand', 'car__model', 'title', ]
    list_filter = ['name', 'category__cat_name', 'category__group__cat_group_name']
    ordering = ["-id"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(CategoryGroup)
class CategoryGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'rating']
    search_fields = ['author', 'product__name']
    list_filter = ['author', 'product__name', 'rating']
    ordering = ["-id"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'merch']
    list_filter = ['title', 'merch__name']
    ordering = ["-id"]


class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def products_count(self, obj):
        return obj.products.count()

    products_count.short_description = 'Products count'

    list_display = ['id', 'user', 'products_count', 'created']
    search_fields = ['id', 'user__username', 'user__email', 'products__name']
    list_filter = ['user__username', 'user__email', 'products']
    ordering = ["-created"]

    readonly_fields = ('created',)
    inlines = [OrderDetailsInline]
