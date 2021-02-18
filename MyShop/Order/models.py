from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Order(models.Model):
    create_at = models.DateTimeField(_("create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("update at"), auto_now_add=True)
    description = models.TextField(_("description"), default='order', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.CASCADE,
                             related_name='order',
                             related_query_name='order')

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def __str__(self):
        return self.user.first_name

    @property
    def get_cart_total(self):
        order_items = OrderItem.objects.all()
        total = sum([item.total_price for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = OrderItem.objects.all()
        total = sum([item.count for item in order_items])
        return total

    @property
    def total_sum_price(self):
        t_price = 0
        item_list = self.order.all()
        for item in item_list:
            t_price += item.total_price
        return t_price

class OrderItem(models.Model):
    count = models.IntegerField(_("count"), default=0)
    price = models.IntegerField(_("price"), default=0)
    order = models.ForeignKey("Order.Order", verbose_name=_('order'), on_delete=models.CASCADE,
                              related_name='order', related_query_name='order')
    shop_product = models.ForeignKey("Product.ShopProduct", verbose_name=_('shop_product'), on_delete=models.CASCADE,
                                     related_name='shop_product', related_query_name='shop_product')

    class Meta:
        verbose_name = _('orderItem')
        verbose_name_plural = _('orderItems')

    def __str__(self):
        return self.shop_product.product.name

    @property
    def total_price(self):
        return int(self.shop_product.price) * int(self.count)



class Payment(models.Model):
    amount = models.IntegerField(_('amount'), )
    order = models.OneToOneField('Order.Order', verbose_name=_('order'), on_delete=models.CASCADE,
                                 related_name='payment', related_query_name='payment')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('user'), on_delete=models.CASCADE,
                             related_name='payment', related_query_name='payment')

    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def __str__(self):
        return self.amount


class Basket(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('user'), on_delete=models.CASCADE,
                                related_name='basket', related_query_name='basket')

    class Meta:
        verbose_name = _('basket')
        verbose_name_plural = _('baskets')

    def __str__(self):
        return self.user.first_name


class BasketItem(models.Model):
    price = models.IntegerField(_('price'), )
    basket = models.ForeignKey('Order.Basket', verbose_name=_('basket'), on_delete=models.CASCADE,
                               related_name='basketItem', related_query_name='basketItem')
    shop_product = models.ForeignKey('Product.ShopProduct', verbose_name=_('shop_product'), on_delete=models.CASCADE,
                                     related_name='basketItem', related_query_name='basketItem')

    class Meta:
        verbose_name = _('basketItem')
        verbose_name_plural = _('basketItems')

    def __str__(self):
        return self.price
