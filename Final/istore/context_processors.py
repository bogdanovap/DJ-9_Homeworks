from .models import CategoryGroup, Category


# TODO: add caching
# TODO: add store name to settings, context, header, footer
def nav_menu(request):
    menu_group = CategoryGroup.objects.all()
    menu_no_group = Category.objects.all().filter(group__isnull=True)

    return {
        'menu_group': menu_group,
        'menu_no_group': menu_no_group,
    }
