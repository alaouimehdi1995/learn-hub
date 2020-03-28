# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    fields = (
        "email",
        "username",
        "password",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "groups",
    )
