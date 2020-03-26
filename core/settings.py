# -*- coding: utf-8 -*-

from enum import Enum
import os


class EnvironmentType(str, Enum):
    LOCAL = "local"
    TEST = "test"
    PRODUCTION = "production"


### Global Project Variables #########################################

# The base directory of the project is the current one
BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))

# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = "/static/"
ROOT_URLCONF = "urls"

# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

### Environment Related Variables ####################################

ENV_TYPE: str = os.environ.get("ENV_TYPE", EnvironmentType.LOCAL)
DEBUG: bool = ENV_TYPE != EnvironmentType.PRODUCTION

# The django secret_key should be unique for each django application,
# and shouldn't change during the runtime.
# For `production` environment, it should be set as environment variable
# For the other environments (local and test), if the env variable
# `DJANGO_APP_SECRET_KEY` doesn't exist, it's generated then saved in
# `.django_secret_key` file for further use.
SECRET_KEY_FILE_PATH: str = os.path.join(BASE_DIR, "./.django_secret_key")
if (
    not os.environ.get("DJANGO_APP_SECRET_KEY")
    and ENV_TYPE != EnvironmentType.PRODUCTION
):
    try:  # Reading `.django_secret_key` if it exists
        with open(SECRET_KEY_FILE_PATH, "r") as f:
            secret_key: str = f.read()
    except OSError:  # In case it doesn't, generating the key and saving it in `.django_secret_key`
        from django.core.management.utils import get_random_secret_key

        secret_key: str = get_random_secret_key()
        with open(SECRET_KEY_FILE_PATH, "w") as f:
            f.write(secret_key)

    os.environ["DJANGO_APP_SECRET_KEY"] = secret_key
SECRET_KEY: str = os.environ["DJANGO_APP_SECRET_KEY"]


### Database ########################################################

# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": "5432",
    }
}

### Applications Settings ###########################################

ALLOWED_HOSTS = []
WSGI_APPLICATION = "wsgi.application"

# TODO: Drop all useless apps and middlewares
INSTALLED_APPS = [
    # Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",  # For django-admin section
    "django.contrib.messages",  # For django-admin section
    "django.contrib.staticfiles",  # For django-admin section
    # Third-Party Apps
    "rest_framework",
    "rest_framework.authtoken",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",  # For django-admin
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",  # For django-admin
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication"
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
}

# Used for the django-admin section
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]
