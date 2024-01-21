from django.http import HttpResponse
import django.shortcuts
from django.core.handlers.wsgi import WSGIRequest
from basket.models import Basket, Cart
from django.shortcuts import redirect
from django.core import serializers
from basket.utilis import get_or_create_user_basket
from goods.models import Products

def checkout(request:WSGIRequest):
    basket = Basket.objects.filter(user=request.user).filter(archival=False).first()
    basket.archival = True
    basket.save()
    return redirect(request.META['HTTP_REFERER'])


def edit_cart_quantity(request:WSGIRequest):
    if request.method == 'POST':
        id = request.POST['id']
        cart = Cart.objects.get(id=id)
        if cart.basket.user == request.user:
            quantity = int(request.POST['value'])
            if quantity>0 and quantity != cart.quantity and quantity<9999:
                cart.quantity = quantity
                cart.save()
                serialized_object = serializers.serialize('json', [cart.product,])
                return HttpResponse(serialized_object)
        return HttpResponse(status=403)
    else:
        return HttpResponse(status=404)
    
def cart_delete(request:WSGIRequest):
    if request.method == 'POST':
        id = request.POST['id']
        cart = Cart.objects.get(id=id)
        if cart.basket.user == request.user:
            cart.delete()
            return HttpResponse(status=200)
        return HttpResponse(status=403)
    else:
        return HttpResponse(status=404)
    
    
def add_product_to_basket(request:WSGIRequest):
    basket: Basket = get_or_create_user_basket(request)
    product = Products.objects.get(id=request.POST['id'])
    cart, is_create = Cart.objects.get_or_create(basket=basket, product=product, quantity=1)
    return HttpResponse(status=201)

