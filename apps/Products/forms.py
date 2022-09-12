from django.forms import ModelForm
from apps.Products.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_image', 'length', 'width', 'height', 'weight', 'weight_unit', 'description']
