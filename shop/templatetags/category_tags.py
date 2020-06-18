from django import template

from shop.models import Category


register = template.Library()


@register.inclusion_tag('shop/category_tree.html', takes_context=True)
def show_category(context):
    return {'categories': Category.objects.all()}
