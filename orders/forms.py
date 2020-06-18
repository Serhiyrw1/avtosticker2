from django import forms
from phonenumber_field.modelfields import PhoneNumberField

from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model= Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'viber', 'city', 'posta', 'sklad']