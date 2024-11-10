from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import OrderForm
from django.core.mail import send_mail
from django.conf import settings

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})


def order_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            # Отправка email (если настроено)
            send_order_confirmation_email(order)

            return redirect('order_success', order_id=order.id)
        else:
            print(form.errors)  # Вывод ошибок формы для отладки
    else:
        form = OrderForm()

    return render(request, 'shop/order_create.html', {'form': form, 'product': product})


def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    product = order.product  # Получаем продукт, связанный с заказом
    return render(request, 'shop/order_success.html', {'order': order, 'product': product})

def send_order_confirmation_email(order):
    subject = 'Ваш заказ подтверждён!'
    message = f'Спасибо за ваш заказ! Номер вашего заказа: {order.id}. Мы скоро свяжемся с вами для подтверждения.'
    recipient_list = [order.email]
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)