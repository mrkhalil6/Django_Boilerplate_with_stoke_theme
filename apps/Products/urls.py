# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path

from apps.Products import views

urlpatterns = [

    # The home page
    path('', views.ProductView.as_view(), name='products'),
    path('add_product/', views.AddProductView.as_view(), name='products'),

]
