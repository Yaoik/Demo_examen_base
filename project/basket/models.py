from django.db import models
from goods.models import Products
from users.models import CustomUser


# class CartQueryset(models.QuerySet):
#     
#     def total_price(self):
#         return sum(cart.products_price() for cart in self)
#     
#     def total_quantity(self):
#         if self:
#             return sum(cart.quantity for cart in self)
#         return 0
    
    
class Basket(models.Model): 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    archival = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Корзина {self.user.email} | Архивная:{self.archival}'
    
    def carts(self):
        return Cart.objects.filter(basket=self)
    
    def total_price(self):
        return sum(cart.products_price() for cart in self.carts())


class Cart(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name='Корзина')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    #objects = CartQueryset().as_manager()

    def products_price(self):
        return round(self.product.price * self.quantity, 2)

    def __str__(self):
        return f'Корзина {self.basket.user} |Товар {self.product.name} | Количество {self.quantity}'