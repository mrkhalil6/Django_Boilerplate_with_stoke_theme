import os

from django.core.files import File
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from apps.Products.forms import ProductForm
from apps.Products.models import Product


class ProductView(LoginRequiredMixin, View):
    def get(self, request):
        entity = Product.objects.all()
        context = {
            "products": entity
        }
        return render(request, 'products/products_listing.html', context)


class AddProductView(LoginRequiredMixin, View):
    def get(self, request):
        # entity = Product.objects.all()
        # context = {
        #     "products": entity
        # }
        return render(request, 'products/add_product.html')

    def post(self, request):
        # print(request.body)
        # print(request.FILES['product_image'])
        print(request.POST)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        # entity = ProductSerializer(data=request.POST, context=request)
        # if entity.is_valid():
        #     x = entity.save()
        #     x.product_image.save("products", File(open(request.FILES['product_image'], 'rb')))
        # else:
        #     print(entity.errors)
        return render(request, 'products/add_product.html')

