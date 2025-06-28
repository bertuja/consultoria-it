# consultoriait/core/urls.py
from django.contrib import admin
from django.urls import path, include
from core.views import about_view, home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('pages/', include('services.urls')),
    path('accounts/', include('accounts.urls')),  # ✅ usamos include
    path('about/', about_view, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
