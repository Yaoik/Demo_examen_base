from basket.models import Cart, Basket
from django.core.handlers.wsgi import WSGIRequest
from goods.models import Products

def get_user_basket(request):
    return Basket.objects.filter(user=request.user)
    return Cart.objects.filter(user=request.user).select_related('product')

def get_or_create_user_basket(request):
    basket = Basket.objects.filter(user=request.user).filter(archival=False).first()
    if basket:
        return basket

    return Basket.objects.create(user=request.user, archival=False)

def is_product_in_basket(requests:WSGIRequest, product:Products):
    basket = get_or_create_user_basket(requests)
    return product in [i.product for i in basket.carts()]