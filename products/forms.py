# -*- coding: utf-8 -*

from django.forms import ModelForm
from products.models import Product

# Fields
from django.forms import TextInput, Select, Textarea, DateInput, NumberInput, CheckboxInput

class ProductCreateForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'category': Select(attrs={'class': 'form-control', 'id': 'inputCategory'}),
            'title': TextInput(attrs={'class': 'form-control', 'id': 'inputTitle'}),
            'description': Textarea(attrs={'class': 'form-control', 'id': 'inputDescritption'}),
            'expiry_date': DateInput(attrs={'class': 'form-control', 'id': 'inputExpiryDate'}),
            'quantity': NumberInput(attrs={'class': 'form-control', 'id': 'inputQuantity'}),
            'is_opened': CheckboxInput(attrs={'class': 'form-control', 'id': 'inputIsOpened'}),
        }
