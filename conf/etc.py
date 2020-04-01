import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .core import env, DEBUG

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

if not DEBUG:
    REST_FRAMEWORK['EXCEPTION_HANDLER'] = 'app.error_handlers.custom_exception_handler'

SENTRY_DSN = env('SENTRY_DSN', default='')
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[
            DjangoIntegration(),
        ]
    )
