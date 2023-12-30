import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.realpath ( os.path.relpath ( __file__ ) )

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Host
ALLOWED_HOSTS = ['*']

# Application definition
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

WSGI_APPLICATION = 'blogdjango.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dbBlog'),
    }
}

# Password validation
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
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_ROOT = 'media'
MEDIA_URL = '/post/'
STATIC_ROOT = ''

# Login
from django.conf.global_settings import LOGIN_REDIRECT_URL
LOGIN_REDIRECT_URL = '/login'
LOGOUT_REDIRECT_URL  = '/'
LOGIN_URL = 'login'

# Messages
from django.contrib import messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info' ,
    messages.INFO: 'alert-info' ,
    messages.SUCCESS: 'alert-success' ,
    messages.WARNING: 'alert-warning' ,
    messages.ERROR: 'alert-danger' ,
}

# DATE_INPUT_FORMATS
# DATE_INPUT_FORMATS = ['%Y-%m-%d %H:%M:%S']
