# coding: utf-8
from django.db.models import ProtectedError
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import exception_handler
from sentry_sdk import capture_exception


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    code = getattr(response, 'status_code', HTTP_500_INTERNAL_SERVER_ERROR)
    if code == HTTP_500_INTERNAL_SERVER_ERROR:
        capture_exception(exc)

    if isinstance(exc, ProtectedError):
        protected_objects = exc.protected_objects
        errors = {'non_field_errors': [
            f'This object is referenced in other objects: {", ".join([str(x) for x in protected_objects])}'
        ]}
    else:
        errors = getattr(response, 'data', {'non_field_errors': [str(exc)]})

    return Response(errors, status=code)
