from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Каталог товаров
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Страница товара
    path('order/create/<int:product_id>/', views.order_create, name='order_create'),  # Оформление заказа
    path('order/success/<int:order_id>/', views.order_success, name='order_success'),  # Подтверждение заказа
]