"""
Django settings for civiwiki project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os, json
from django.core.exceptions import ImproperlyConfigured
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(BASE_DIR, "utils/secrets.json")) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    if secrets:
        try:
            return secrets[setting]
        except KeyError:
            error = "{setting} is not a key in the secrets.json file".format(setting=setting)
            raise ImproperlyConfigured(error)
    else:
        error = "Please configure your secrets.json file".format(setting=setting)
        raise ImproperlyConfigured(error)

SECRET_KEY = get_secret("SECRET_KEY")
ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'api',
	'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
	'corsheaders.middleware.CorsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'civiwiki.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "../frontend/templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'civiwiki.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
if 'RDS_DB_NAME' in os.environ:

    DATABASE = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.enviorn['RDS_DB_NAME'],
            'USER': os.enviorn['RDS_USERNAME'],
            'PASSWORD': os.enviorn['RDS_PASSWORD'],
            'HOST': os.enviorn['RDS_HOSTNAME'],
            'PORT': os.enviorn['RDS_PORT']
        }
    }

else:

    DEBUG = True

    DATABASES = {
        "default": {
            "HOST": get_secret("DATABASE_HOST"),
            "POST": get_secret("DATABASE_PORT"),
            "NAME": get_secret("DATABASE_NAME"),
            "ENGINE": get_secret("DATABASE_ENGINE"),
            "USER": get_secret("DATABASE_USER"),
            "PASSWORD": get_secret("DATABASE_PASSWORD")
        }
    }


EMAIL_HOST = get_secret("EMAIL_HOST")
EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")
EMAIL_PORT = get_secret("EMAIL_PORT")
EMAIL_USE_TLS = get_secret("EMAIL_USE_TLS")

LOGIN_URL = '/login'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False #Eh deal with timezones on front-end, I dislike them

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "../frontend/static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_ROOT_URL = '/media/'
