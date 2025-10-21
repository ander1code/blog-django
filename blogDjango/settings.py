import os
from pathlib import Path
from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.contrib import messages

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Alternative project path using os (legacy style)
PROJECT_PATH = os.path.realpath(os.path.relpath(__file__))

# --------------------------------------------------
# Security Settings
# --------------------------------------------------

# WARNING: Keep the secret key used in production secret!
# SECRET_KEY = ''

# WARNING: Don't run with debug turned on in production!
DEBUG = True

# Hosts allowed to access the application
ALLOWED_HOSTS = ['*']

# --------------------------------------------------
# Application Definition
# --------------------------------------------------

INSTALLED_APPS = [
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogdjango.urls'

WSGI_APPLICATION = 'blogdjango.wsgi.application'

# --------------------------------------------------
# Templates Configuration
# --------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_PATH + "templates"],
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

# --------------------------------------------------
# Database Configuration
# --------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dbblog'),
    }
}

# --------------------------------------------------
# Password Validation
# --------------------------------------------------

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

# --------------------------------------------------
# Internationalization
# --------------------------------------------------

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False

# --------------------------------------------------
# Static and Media Files
# --------------------------------------------------

# URL to access static files
STATIC_URL = '/static/'

# Directory to collect static files (empty means default)
STATIC_ROOT = ''

# URL to access media files
MEDIA_URL = '/media/'

# Directory to store uploaded media files
MEDIA_ROOT = BASE_DIR / 'media'

# --------------------------------------------------
# Authentication Redirects
# --------------------------------------------------

LOGIN_REDIRECT_URL = '/login'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = 'login'

# --------------------------------------------------
# Message Tags
# --------------------------------------------------

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# --------------------------------------------------
# Date Input Formats (optional)
# --------------------------------------------------

# DATE_INPUT_FORMATS = ['%Y-%m-%d %H:%M:%S']
