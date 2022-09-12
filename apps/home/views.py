# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect


@login_required(login_url="/login/")
def index(request):
    req_user = request.user
    user_full_name = req_user.get_full_name()
    image = req_user.user_image
    user_image = request.build_absolute_uri(image)
    user_type = req_user.get_user_type()

    context_details = {
        'user': user_full_name,
        'user_image': user_image,
        'user_type': user_type
    }

    if user_type == "Admin":
        return render(request, "home/dashboard-saas.html", context_details)
    elif user_type == "User":
        return render(request, "home/dashboard-saas.html", context_details)
    elif user_type == "Service Provider":
        return render(request, "home/dashboard-saas.html", context_details)
    else:
        return HttpResponse(status=403)


