# coding: utf-8
from django.http import HttpResponse


def handler404(request, exception, **kwargs):
    return HttpResponse('{"detail":"Not found", "status_code": 404}', content_type='application/json', status=404)


def handler500(request, **kwargs):
    return HttpResponse('{"detail":"Server error", "status_code": 500}', content_type='application/json', status=500)


def trigger_error(request):
    division_by_zero = 1 / 0  # noqa
