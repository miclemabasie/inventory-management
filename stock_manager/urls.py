

from django.contrib import admin
from django.urls import path, include
from accounts.views import dashboard
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls', namespace='products')),
    path('sales/', include('sales.urls', namespace='sales')),
    path('customers/', include('customers.urls', namespace='customers'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
