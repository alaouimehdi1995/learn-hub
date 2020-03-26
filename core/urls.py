# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth-token/", obtain_auth_token, name="api_auth_token"),
]
