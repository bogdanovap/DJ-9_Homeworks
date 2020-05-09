from django import template

register = template.Library()

current_page = "home"

@register.simple_tag(takes_context=True)
def set_page_context(context, page):
    context.dicts[0]['page']=page
    return ''
