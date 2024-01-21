from django import template

from basket.models import Cart
from basket.utilis import get_user_basket, get_or_create_user_basket, is_product_in_basket



register = template.Library()


@register.simple_tag()
def user_basket(request):
    return get_user_basket(request)

@register.simple_tag()
def user_basket_active(request):
    return get_or_create_user_basket(request)

@register.simple_tag()
def product_in_basket(request, product):
    return is_product_in_basket(request, product)