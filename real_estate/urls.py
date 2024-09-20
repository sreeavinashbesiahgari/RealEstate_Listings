from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from listings.views import (listing_list, listing_retrieve,listing_create,listing_update , listing_delete)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listings/<pk>/', listing_retrieve),  # <int:pk> ensures the primary key is treated as an integer
    path('addlisting/', listing_create),
    path('listings/<pk>/edit/', listing_update),
    path('listings/<pk>/delete/', listing_delete)
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
