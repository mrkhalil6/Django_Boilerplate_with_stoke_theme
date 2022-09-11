# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
import string

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template.loader import get_template
from django.urls import reverse

from common.methods import random_key_generator
from ThreePLDashboard import secrets
from .forms import LoginForm, SignUpForm
from django.contrib import messages

from .models import User


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.status != 2:
                    msg = 'Account Deactivated'
                else:
                    login(request, user)
                    return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    # return render(request, "accounts/login.html", {"form": form, "msg": msg})
    return render(request, "accounts/auth-login-2.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "../../templates/accounts/register.html", {"form": form, "msg": msg, "success": success})


def reset_password(request):
    # return render(request, "accounts/login.html", {"form": form, "msg": msg})
    if request.method == "POST":
        request_body = request.POST
        print(request_body)
        user_email = request_body.get("user_email", None)
        if user_email:
            user = User.objects.filter(email__iexact=user_email).first()
            secret_token = random_key_generator(size=6, chars=string.digits)
            user.secret_token = secret_token
            user.save()
            # name = user.get_full_name()
            try:
                server_url = secrets.SERVER_URL
                html_template = get_template('../../templates/common/password_reset.html')
                context_data = {'email': user_email, "secret_token": secret_token, "server_url": server_url}
                html_content = html_template.render(context_data)
                send_mail(
                    subject='Grad Studio Password Reset Instructions',
                    # message="Hello {}, please use the following code to reset the password: {}".format(str(name),
                    #                                                                                 secret_token),
                    message="",
                    from_email=secrets.FROM_EMAIL,
                    recipient_list=[user_email],
                    html_message=html_content,
                    fail_silently=False,

                )
                messages.info(request, "Please check your email for further instructions.")
                return render(request, "../../templates/accounts/password_reset.html")

            except Exception as send_mail_exc:
                print(send_mail_exc)
                messages.error(request, 'Email sending failed.')
                return render(request, "../../templates/accounts/password_reset.html")

        else:
            messages.error(request, "Please provide email address.")
            return render(request, "../../templates/accounts/password_reset.html")
    return render(request, "../../templates/accounts/password_reset.html")


def change_password(request):
    if request.method == "POST":
        request_body = request.POST
        # print(request_body)
        email = request_body.get("email", None)
        secret_token = int(request_body.get("secret_token", None))
        new_password = request_body.get("new_password", None)
        if email and secret_token and new_password:
            user = User.objects.filter(email__iexact=email, secret_token=secret_token).first()
            if user:
                secret_token = random_key_generator(size=6, chars=string.digits)
                user.set_password(new_password)
                user.secret_token = secret_token
                user.save()
                messages.info(request, "Password Successfully Changed !")
                return render(request, "../../templates/accounts/password_change.html")
            else:
                messages.error(request, "Cannot find an associated user.")
                return render(request, "../../templates/accounts/password_change.html")
        return render(request, "../../templates/accounts/password_change.html")
    else:
        request_params = request.GET
        email = request_params.get("email", None)
        secret_token = request_params.get("secret_token", None)
        if email and secret_token:
            context = {"email": email, "secret_token": secret_token}
            return render(request, "../../templates/accounts/password_change.html", context)
        else:
            return render(request, "../../templates/home/page-403.html")


def email_confirmation(request):
    if request.method == "POST":
        print(request.POST)
        request_body = request.POST
        email = request_body.get("email", None)
        secret_token = request_body.get("secret_token", None)
        new_password = request_body.get("new_password", None)
        if email and secret_token and new_password:
            new_secret_token = random_key_generator(size=6, chars=string.digits)
            user = User.objects.filter(email=email, secret_token=secret_token, status=1).first()
            if user:
                user.secret_token = new_secret_token
                user.status = 2
                user.set_password(new_password)
                user.save()

                return redirect(reverse('login'))
            else:
                messages.error(request, "Invalid Request")
                return render(request, "../../templates/home/page-403.html")
        else:
            messages.error(request, "Invalid Request")
            return render(request, "../../templates/home/page-403.html")
    else:
        request_params = request.GET
        email = request_params.get("email", None)
        secret_token = request_params.get("secret_token", None)
        if email and secret_token:
            context = {"email": email, "secret_token": secret_token}
            return render(request, "../../templates/accounts/auth-confirm-mail-2.html", context)
        else:
            return render(request, "../../templates/home/page-500.html")
