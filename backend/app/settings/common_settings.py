# -*- coding: utf-8 -*-
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get("DJANGO_DEVELOPMENT_SECRET_KEY", "admin")

DEBUG = int(os.environ.get("DEBUG", default=False))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
ALLOWED_HOSTS = '127.0.0.1'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # https://docs.djangoproject.com/en/4.2/ref/contrib/postgres/
    'django.contrib.postgres',   
    # https://docs.djangoproject.com/en/4.2/ref/contrib/sites/
    'django.contrib.sites',
    # https://docs.djangoproject.com/en/4.2/ref/contrib/sitemaps/
    'django.contrib.sitemaps',
    # https://docs.djangoproject.com/en/4.2/ref/contrib/humanize/
    'django.contrib.humanize', # tempaltes numbers and some dates
]

RECENT_APPS = [
    # https://www.django-rest-framework.org/tutorial/quickstart/
    'rest_framework',
]
INSTALLED_APPS += RECENT_APPS

LOCAL_APPS = [
    
]
INSTALLED_APPS += LOCAL_APPS

# Id Site
SITE_ID = 1

# Middlewares definition
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

RECENT_MIDDLEWARE = [

]
MIDDLEWARE += RECENT_MIDDLEWARE

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            ],
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

# Path where locate error html pages 
ERRORS_TAMPLATES_PATH = 'errors'

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static Files
# https://docs.djangoproject.com/en/4.2/ref/settings/#static-url
STATIC_URL = 'static/'

# https://docs.djangoproject.com/en/4.2/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# https://docs.djangoproject.com/en/4.2/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'other_static/'),
]

# https://docs.djangoproject.com/en/4.2/ref/settings/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Media Files
# https://docs.djangoproject.com/en/4.2/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# https://docs.djangoproject.com/en/4.2/ref/settings/#media-url
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
