from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from .errors.views import page_not_found_view_404
from .errors.views import page_internal_server_error_500

# Main urls
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Erros pages
handler404 = page_not_found_view_404
handler500 = page_internal_server_error_500

# Debuging
if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
    urlpatterns += (path("debug/", include("debug_toolbar.urls")),)