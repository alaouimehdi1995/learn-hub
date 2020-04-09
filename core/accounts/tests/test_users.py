# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model

from accounts.models import User


def test_default_user_model_is_custom():
    assert get_user_model() == User
