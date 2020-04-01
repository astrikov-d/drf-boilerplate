from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic.base import RedirectView

from app.error_handlers.views import trigger_error

handler404 = 'app.error_handlers.views.handler404'
handler500 = 'app.error_handlers.views.handler500'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('admin:index')), name='home'),
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
]
