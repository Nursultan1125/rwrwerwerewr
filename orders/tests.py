from django.test import TestCase

# Create your tests here.
from orders.models import Order, OrderItem
from product.models import Product


class OrderItemTest(TestCase):
    def setUp(self):
        self.product = Product(product_name="Arduino", product_image="",
                               product_prices=750, product_overview="aeqweq")
        self.order = Order(first_name='N', last_name='Zh', email='m@mail.ru', address='S', city='Bishkek')
        self.order_item = OrderItem(order=self.order, product=self.product, price=100, count=10)

    def test_get_cost(self):
        self.assertEqual(self.order_item.get_cost(), 1000)


class OrderTest(TestCase):
    def setUp(self):
        self.product = Product(product_name="Arduino", product_image="",
                               product_prices=750, product_overview="aeqweq")
        self.product.save()
        self.order = Order(first_name='N', last_name='Zh', email='m@mail.ru', address='S', city='Bishkek')
        self.order.save()

    def test_get_total_cost(self):
        for item in range(10):
            order_item = OrderItem(order=self.order, product=self.product, price=1, count=1)
            order_item.save()
        self.assertEqual(self.order.get_total_cost(), 10)

    def test_get_total_cost_product_different_price(self):
        for item in range(10):
            product = Product(product_name=str(item), product_image="",
                              product_prices=5 * item, product_overview=str(item))
            product.save()
            order_item = OrderItem(order=self.order, product=product, price=product.product_prices, count=1)
            order_item.save()
            #
        self.assertEqual(self.order.get_total_cost(), 225)

    def test_get_total_cost_product_different_count(self):
        for item in range(10):
            product = Product(product_name=str(item), product_image="",
                              product_prices=5 * item, product_overview=str(item))
            product.save()
            order_item = OrderItem(order=self.order, product=product, price=product.product_prices, count=item)
            order_item.save()
            #
        self.assertEqual(self.order.get_total_cost(), 1425)
