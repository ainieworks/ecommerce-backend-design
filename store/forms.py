from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        # Which model this form is based on
        model = Product
        # Which fields appear in the form
        fields = ['name', 'description', 'price', 'category', 'image', 'stock']
        labels = {
            'name': 'Product Name',
            'stock': 'Available Stock',
        }