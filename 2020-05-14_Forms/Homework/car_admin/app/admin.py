from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ['brand', 'model', 'review_count', ]
    ordering = ["-id"]


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ['car', 'title', ]
    search_fields = ['car__brand', 'car__model', 'title', ]
    list_filter = ['car__brand', 'car__model', 'title', ]
    ordering = ["-id"]


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
