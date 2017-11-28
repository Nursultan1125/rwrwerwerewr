from django.core.mail import send_mail

from orders.models import Order


def OrderCreated(order_id):
    order = Order.objects.get(id=order_id)
    subject = "Звказ от %s %s с номером %d" % (order.users.first_name, order.users.last_name, order.id)
    message = "Список товаров: "
    for item in order.items.all():
        message += " Товар %s количество %s Цена %s \n" % (item.product.product_name,
                                                        item.count, item.get_cost())
    mail_send = send_mail(subject, message, 'provervka@mail.com', ['zholnurs@gmail.com'])
    return mail_send