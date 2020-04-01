import os

import environ

from .apps import DJANGO_APPS, PROJECT_APPS, THIRD_PARTY_APPS

root = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env(root('.env'))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))


def unquote_env_variable(v):
    if len(v):
        if v[0] == v[-1] in ['"', "'"]:
            v = v[1:-1]
    return v


SECRET_KEY = unquote_env_variable(env('DJANGO_SECRET_KEY', default='secret'))
DEBUG = env.bool('DEBUG', default=False)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = [env('ALLOWED_HOST', default='localhost')]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates'),
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

WSGI_APPLICATION = 'srv.wsgi.application'

DATABASES = {
    'default': env.db(),
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True

DATE_FORMAT = 'd/m/Y'

DATETIME_FORMAT = 'd/m/Y H:i'

TIME_FORMAT = 'H:i:s'

FIRST_DAY_OF_WEEK = 1

STATIC_HOST = env('DJANGO_STATIC_HOST', default='')
STATIC_URL = STATIC_HOST + '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'app/static')

STATICFILES_DIRS = []

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
ENABLE_SQL_LOG = env.bool('DJANGO_DEBUG_SQL', default=False)
if ENABLE_SQL_LOG:
    LOGGING['handlers'].update({
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    })
    LOGGING['loggers'].update({
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    })

FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600
DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600
