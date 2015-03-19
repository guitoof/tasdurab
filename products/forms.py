# -*- coding: utf-8 -*

from django.forms import ModelForm
from products.models import Product

# Fields
from django.forms import TextInput, Select, Textarea, DateInput, NumberInput, CheckboxInput

class ProductCreateForm(ModelForm):

    class Meta:
        model = Product
        exclude = ('owner',)
        widgets = {
            'category': Select(attrs={'class': 'form-control', 'id': 'input-category'}),
            'title': TextInput(attrs={'class': 'form-control', 'id': 'input-title'}),
            'description': Textarea(attrs={'class': 'form-control', 'id': 'input-descritption', 'rows': '3'}),
            'expiry_date': DateInput(attrs={'class': 'form-control', 'id': 'input-expiry_date', 'placeholder': 'jj/mm/aaaa'}),
            'quantity': NumberInput(attrs={'class': 'form-control', 'id': 'input-quantity'}),
            'is_opened': CheckboxInput(attrs={'id': 'input-is_opened' }),
        }
