# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="/login/")
def index(request):
    req_user = request.user.get_full_name()

    context_details = {
        'user': req_user,
    }
    return render(request, "home/dummy.html", context_details)
