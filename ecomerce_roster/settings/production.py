# settings.py

from pathlib import Path
import os
import datetime
import dj_database_url

# PATH CONFIGURATION
# ------------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = BASE_DIR.parent

# Site name:
SITE_NAME = BASE_DIR.name

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
import sys
sys.path.append(str(BASE_DIR))


# DEBUG CONFIGURATION
# ------------------------------------------------------------------------------
DEBUG = True


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
SECRET_KEY = '!!a8)if_&%(z3$mfhi0obg!a077x-tqbud(6#ky$we^v*r85ca'


# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
ADMINS = [
    ('Miguel A. Tribaldos', 'mtribaldos@gmail.com'),
]


# SITE CONFIGURATION
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ['*']


# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
FIXTURE_DIRS = [
    BASE_DIR / 'fixtures',
]


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URL CONFIGURATION
# ------------------------------------------------------------------------------
ROOT_URLCONF = f'{SITE_NAME}.urls'


# Application definition
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'bootstrapform',
    'bootstrap_datepicker',
]

LOCAL_APPS = [
    'roster',
    'django.contrib.admin',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS


# WSGI CONFIGURATION
# ------------------------------------------------------------------------------
WSGI_APPLICATION = f'{SITE_NAME}.wsgi.application'


# Password validation
# ------------------------------------------------------------------------------
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


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'es'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Database configuration for development
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Database configuration for production
# ------------------------------------------------------------------------------
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Additional settings
# ------------------------------------------------------------------------------
SHIFT_GROUP_NAME = 'Guardias'
SHIFT_CARDINALITY = 1000
SHIFT_USERS = ['mtribaldos', 'jorgecremades', 'mortega', 'dgalera', 'pacoma']
ANCHOR_DATE = datetime.date(2016, 1, 1)
LOGIN_REDIRECT_URL = "/"
