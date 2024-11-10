from django import forms
from .models import Order, OrderItem, Product



from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    email = forms.EmailField(label='Email', max_length=254)

    class Meta:
        model = Order
        fields = ['email']  # Оставляем только поле email