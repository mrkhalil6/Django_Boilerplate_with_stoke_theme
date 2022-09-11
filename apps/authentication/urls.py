# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, reset_password, change_password, email_confirmation
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('reset_password/', reset_password, name="reset_password"),
    path('change_password/', change_password, name="change_password"),
    path('email_confirmation/', email_confirmation, name="email_confirmation"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
]
