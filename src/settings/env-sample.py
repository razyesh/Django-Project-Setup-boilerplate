from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "<generated_secret_key>"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "<db_name>",
        "USER": "<db_user>",
        "PASSWORD": "<db_password>",
        "HOST": "<db_host>",
        "PORT": "<db_port>",
    },
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "<email_host>"
EMAIL_PORT = 587
EMAIL_HOST_USER = "<email_host_user>"
EMAIL_HOST_PASSWORD = "<email_host_password>"
EMAIL_SENDER = "<email_sender>"
